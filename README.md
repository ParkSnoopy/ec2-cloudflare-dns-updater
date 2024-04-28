
# AWS EC2 - Cloudflare DNS Updater

Dns update script for Amazon EC2 Instance


### Test Environment
* Amazon AWS EC2 instance (ubuntu server 22.04 LTS)
* Cloudflare DNS Service (API)

## Disclaimer

This project is just personal hobby project


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
   Replace value `CLOUDFLARE_ZONEID = " /* paste zone id here */ "`

4. Create API token according to [this Cloudflare Docs](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)
   Replace value `CLOUDFLARE_DNS_EDIT_APIKEY = " /* paste cloudflare api token here */ "`

5. Change `'name'` of each `TARGET_DNSINFOS` into **Your Domain Name**
>  Change `COMMENT` or `'tags'` if you want to

6. run script

```bash
chmod +x ./init.sh
./init.sh

chmod +x ./update.sh
./update.sh
```

7. add script to crontab

```bash
crontab -e
```
```nano
@reboot /path/to/repository/update.sh
```
