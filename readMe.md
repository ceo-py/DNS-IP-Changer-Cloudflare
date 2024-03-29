# Cloudflare DNS IP Change via API

This Python script automates dynamic DNS updates for Cloudflare-managed domains using Cloudflare's API.
It allows users to update DNS records with new IP addresses seamlessly.
Simply specify the domain and Cloudflare ID in the 'DNS_TO_CHANGE' dictionary, and provide your Cloudflare
account details (email, API key, and zone ID) along with the new IP address to initiate the update process.

## Instructions

1. Replace placeholders `YOUR_EMAIL`, `YOUR_API_KEY`, and `YOUR_ZONE_ID` with your Cloudflare account details.
2. Set `NEW_IP_ADDRESS` to the new IP address that you want to assign to your domains.
3. Run the script to update the DNS records automatically.

**Note:** Ensure that your Cloudflare API key has the necessary permissions to read and edit DNS records.

## Usage

```bash
python main.py
