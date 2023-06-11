import json
import whois

# Define target domain
target = input("Enter target domain: ")

# Perform WHOIS lookup
result = whois.whois(target)

# Convert result to JSON object
data = {
    "domain_name": result.domain_name,
    "creation_date": result.creation_date,
    "expiration_date": result.expiration_date,
    "updated_date": result.updated_date,
    "registrar": result.registrar,
    "registrant": result.registrant,
    "admin": result.admin,
    "tech": result.tech,
    "name_servers": result.name_servers,
    "status": result.status
}

# Write JSON object to file
with open(f"{target}.json", "w") as f:
    json.dump(data, f, indent=4)

print("WHOIS lookup complete.")
# import requests
# from bs4 import BeautifulSoup
# import subprocess
# import re
# from scapy.all import IP
# import socket
# import json

# # Define target domain or IP address
# target = input("Enter target domain or IP address: ")

# # Define whois lookup function
# def whois_lookup(target):
#     command = f"nslookup {target}"
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)

#     if result.returncode == 0:
#         return result.stdout
#     else:
#         return f"Error: {result.stderr}"

# # Define Afrinic WHOIS lookup function
# def afrinic_whois_lookup(target):
#     # Get IP address from target
#     output = whois_lookup(target)
#     ip_address = ""

#     for line in output.splitlines():
#         if "Address:" in line:
#             parts = line.split()
#             ip_address = parts[1]
#             break

#     # Retrieve WHOIS information from Afrinic WHOIS service
#     url = f"https://afrinic.net/whois?searchtext={ip_address}"
#     response = requests.get(url)

#     # Parse WHOIS information into a JSON object
#     data = {}
#     for line in response.text.splitlines():
#         if ":" in line:
#             parts = line.split(":")
#             key = parts[0].strip()
#             value = ":".join(parts[1:]).strip()
#             data[key] = value

#     # Write JSON object to file
#     with open(f"{ip_address}.json", "w") as f:
#         json.dump(data, f, indent=4)

#     return data
# # Call Afrinic WHOIS lookup function
# result = afrinic_whois_lookup(target)
# print(json.dumps(result, indent=4))