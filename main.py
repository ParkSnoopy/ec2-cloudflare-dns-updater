from init import *


def main():
    aws_ec2_token = get_aws_ec2_token()
    pub_ipv4_addr = get_aws_ec2_pubip4(aws_ec2_token)

    for target in TARGET_DNSINFOS:
        target.update({"content": pub_ipv4_addr})

    if dns_list := get_cloudflare_dns_list():
        extracted_id_record = extract_cloudflare_dns_record_id(dns_list, TARGET_DNSINFOS)
    else:
        debug("  ERR : fetch Cloudflare DNS list failed")
        return 1
    for record_id, body in extracted_id_record:
        if not update_cloudflare_dns(record_id, body):
            debug("  ERR : update Cloudflare DNS failed")
            return 1

if __name__ == "__main__":
    print("Update Cloudflare DNS")
    if not main():
        print("DNS Record Update finished Successfully")
