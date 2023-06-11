import socket

def do_whois_request(ip, selected_server):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((selected_server, 43))
    s.send((ip + "\r\n").encode())
    response = b""
    while True:
        data = s.recv(4096)
        response += data
        if not data:
            break
    s.close()
    return response.decode("utf-8", "ignore")

if __name__ == "__main__":
    ip = "197.230.16.18"
    whois_servers = [
        "whois.verisign-grs.com", "whois.registrypro.pro", "whois.nic.mil", "whois.nic.gov",
        "whois.nic.edu", "whois.nic.name", "whois.nic.org", "whois.nic.info", "whois.nic.me",
        "whois.nic.asia", "whois.nic.co", "whois.nic.uk", "whois.nic.fr", "whois.nic.de",
        "whois.nic.it", "whois.nic.au", "whois.nic.br", "whois.nic.jp", "whois.nic.ca",
        "whois.nic.mx", "whois.nic.za", "whois.arin.net", "whois.ripe.net",
        "whois.apnic.net", "whois.afrinic.net",
    ]
    print("Liste des serveurs Whois disponibles :")
    for i, server in enumerate(whois_servers):
        print(f"{i + 1}. {server}")

    choice = input("Veuillez choisir un serveur Whois : ")
    selected_server = whois_servers[int(choice) - 1]

    response = do_whois_request(ip, selected_server)
    print(response)