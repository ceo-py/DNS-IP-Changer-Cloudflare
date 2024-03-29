import requests

# format is domain: id for Cloudflare
DNS_TO_CHANGE = {
    'example.com': 'osjfewoi092344iwokefjweofm02394i',
}

# Replace these variables with your actual data
YOUR_EMAIL = 'Email from Cloudflare Account'
YOUR_API_KEY = 'API Key from Cloudflare with access for DNS to read and edit'
YOUR_ZONE_ID = 'Zone ID from Cloudflare'
NEW_IP_ADDRESS = 'New IP address that will be changed'

headers = {
    'Authorization': f'Bearer {YOUR_API_KEY}',
    'Content-Type': 'application/json',
}


def list_dns_records(zone_id: str) -> None:
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        records = response.json()['result']
        for record in records:
            print(
                f"ID: {record['id']}, Type: {record['type']}, Name: {record['name']}, Content: {record['content']}")
    else:
        print("Failed to retrieve DNS records.")
        print(response.text)


# list_dns_records(YOUR_ZONE_ID)

def update_dns_record(zone_id: str, record_id: str, new_ip: str, domain_name: str) -> None:
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    data = {
        'type': 'A',
        'name': domain_name,
        "content": new_ip,
        'proxied': True
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print("DNS record updated successfully.")
    else:
        print("Failed to update DNS record.")
        print(response.text)


# update_dns_record(YOUR_ZONE_ID, 'osjfewoi092344iwokefjweofm02394i', '0.0.0.0', 'example.com')


def change_dns_ips(new_ip: str) -> None:
    for domain, record_id in DNS_TO_CHANGE.items():
        update_dns_record(YOUR_ZONE_ID, record_id, new_ip, domain)

# change_dns_ips(NEW_IP_ADDRESS)