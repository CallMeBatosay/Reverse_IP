import socket

def domain_to_ip(input_file):
    output_file = f"{input_file.split('.')[0]}_result.txt"
    unique_ips = set()

    try:
        with open(input_file, 'r') as domains_file:
            domains = domains_file.readlines()

            with open(output_file, 'w') as result_file:
                for domain in domains:
                    domain = domain.strip()
                    try:
                        ip_address = socket.gethostbyname(domain)
                        if ip_address not in unique_ips:
                            result_file.write(f"{ip_address}\n")
                            unique_ips.add(ip_address)
                            print(f"Domain: {domain} > IP: {ip_address}")
                        else:
                            print(f"Domain: {domain} > Skipped (Duplicate IP)")
                    except socket.gaierror:
                        print(f"Domain: {domain} > Unable to resolve")

        print(f"Hasil IP telah disimpan ke {output_file}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

def main():
    print("""
    Domain To Ip
          Github   : https://github.com/CallMeBatosay/Reverse_IP
          Telegram : @MyBatosay1337
          Ch       : https://t.me/Prv8Batosay

                    >_@MyBatosay1337
    """)
    input_file = input("Domain List : ")
    domain_to_ip(input_file)

if __name__ == "__main__":
    main()
