from . import main



if __name__ == "__main__":
    print("Updating Cloudflare DNS")
    if not main.main():
        print("DNS Record Update finished Successfully")
