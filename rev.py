import requests
import re

def clean_domain(domain):
    cleaned_domain = re.sub(r'^(www\.|www2\.)', '', domain)
    return cleaned_domain

def reverse_ip_lookup(ip):
    api_url = f"https://api.webscan.cc/?action=query&ip={ip}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        if response.status_code == 200:
            if isinstance(data, list):
                return data
            else:
                print(f"Error: Unexpected API response format for IP: {ip}")
                return None
        else:
            print(f"Error: {data.get('message', 'Unknown error')} for IP: {ip}")
            return None

    except requests.RequestException as e:
        print(f"Error: {e} for IP: {ip}")
        return None

def main():
    print("""
    Reverse IP
          Github   : https://github.com/CallMeBatosay/Reverse_IP
          Telegram : @MyBatosay1337
          Ch       : https://t.me/Prv8Batosay

                    >_@MyBatosay1337
    """)
    file_name = input("List IP : ")

    try:
        with open(file_name, 'r') as ip_file:
            ips = ip_file.readlines()

        output_file = f"{file_name.split('.')[0]}_domain.txt"

        unique_domains = set()

        with open(output_file, 'w') as result_file:
            for ip_address in ips:
                ip_address = ip_address.strip()
                domains = reverse_ip_lookup(ip_address)

                if domains:
                    for domain_info in domains:
                        domain = domain_info.get("domain", "")
                        cleaned_domain = clean_domain(domain)

                        if cleaned_domain not in unique_domains:
                            result_file.write(f"{cleaned_domain}\n")
                            unique_domains.add(cleaned_domain)
                        else:
                            print(f"Skipped duplicate domain: {cleaned_domain}")

        print(f"Hasil domain yang unik telah disimpan ke {output_file}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

if __name__ == "__main__":
    main()
