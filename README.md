
# AWS EC2 - Cloudflare DNS Updater

Dns update script for Amazon EC2 Instance


### Test Environment
* Amazon AWS EC2 instance (ubuntu server 22.04 LTS)
* Cloudflare DNS Service (API)

## Disclaimer

This project is personal hobby project


## Deployment

> All configuration is done in `config.py`
> which is file `config.py.example` renamed into

To deploy this project, 

1. Clone Repository

```bash
gh repo clone ParkSnoopy/aws-ec2-cloudflare-dns-updater
```

2. Rename `config.py.example` to `config.py`

3. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) > Overview > Copy Zone ID 

4. Replace value `CLOUDFLARE_ZONEID = "paste zone id here"`

5. Create API token according to [this Cloudflare Docs](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)

6. Replace value `CLOUDFLARE_DNS_EDIT_APIKEY = "paste cloudflare api token here"`

7. Change `'name'` of each `TARGET_DNSINFOS` to your domain name

8. Change `COMMENT` or `'tags'` if you want to

9. make virtual environment and install dependencies

```bash
# Since `run.sh` optimized for venv name `venv`, use name `venv`
python3 -m venv venv
```

9. run script

```bash
chmod +x ./main.py
```
```bash
./main.py
```

10. if DNS record changed seamlessly, add to crontab

```bash
crontab -e
```

```nano
@reboot /path/to/repository/main.py
```
