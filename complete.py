from config import *


CLOUDFLARE_API_HEADER = {
	"Content-Type": "application/json",
	"Authorization": f"Bearer {CLOUDFLARE_DNS_EDIT_APIKEY}",
}
