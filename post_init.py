import requests
import json

from config import *

CLOUDFLARE_API_HEADER = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CLOUDFLARE_DNS_EDIT_APIKEY}",
}


def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def get_aws_ec2_token():
    debug(f"  PUT : {AWS_EC2_METADATA_URL}")
    AWS_EC2_METADATA_HEADER = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
    aws_ec2_token = requests.put(AWS_EC2_METADATA_URL, headers=AWS_EC2_METADATA_HEADER).text
    debug(f"  RESP: TOKEN={aws_ec2_token[:5]}...")
    return aws_ec2_token

def get_aws_ec2_pubip4(aws_ec2_token):
    debug(f"  GET : {AWS_EC2_PUB_IPv4_URL}")
    AWS_EC2_PUB_IPv4_HEADER = {"X-aws-ec2-metadata-token": aws_ec2_token}
    pub_ipv4 = requests.get(AWS_EC2_PUB_IPv4_URL, headers=AWS_EC2_PUB_IPv4_HEADER).text
    debug(f"  RESP: pub_IPv4={pub_ipv4}")
    return pub_ipv4

def get_cloudflare_dns_list():
    debug(f"  GET : {CLOUDFLARE_DNS_LIST_URL}")
    cloudflare_dns_list = requests.get(
        CLOUDFLARE_DNS_LIST_URL.format(zoneid=CLOUDFLARE_ZONEID),
        headers=CLOUDFLARE_API_HEADER,
    ).json()
    debug(f"  RESP: success={cloudflare_dns_list['success']}")
    if cloudflare_dns_list['success']:
    	return cloudflare_dns_list['result']
    return None

def _find_from_listdict(key, value, items:list[dict]):
    for each in items:
        if key in each and each[key] == value:
            return each

def extract_cloudflare_dns_record_id(dns_list, target_dnsinfos):
    results = list()
    for record in dns_list:
        if not any( record['name'] == target['name'] for target in target_dnsinfos ):
            continue
        if record['type'] == 'A': # Only A record will be updated
            results.append(
                (record['id'], _find_from_listdict('name', record['name'], target_dnsinfos))
            )
    return results

def update_cloudflare_dns(record_id, body):
    # targets: list of DNS info dict in `config.py`
    # content: ip address to change record into

    debug(f"  PUT : {CLOUDFLARE_DNS_UPDATE_URL}")
    update_response = requests.put(
        CLOUDFLARE_DNS_UPDATE_URL.format(zoneid=CLOUDFLARE_ZONEID, recordid=record_id),
        headers=CLOUDFLARE_API_HEADER,
        json=body,
    ).json()
    debug(f"  RESP: success={update_response['success']}")
    if update_response['success']:
        return update_response['result']
    return None
