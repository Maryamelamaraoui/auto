import whois
import dns.resolver
import requests
from bs4 import BeautifulSoup
import subprocess
import requests
import re
from scapy.all import IP

while True:
    try :
        # Define target domain or email address
        target = input("Enter target domain or email address: ")
        if target == "exit":
            break
        # Définir le nom de domaine cible
        domain_name = target

        # Récupérer les enregistrements WHOIS
        w = whois.whois(domain_name)
        print("WHOIS Record:")
        print(w)

        # Récupérer les adresses IP associées au nom de domaine
        answers = dns.resolver.resolve(domain_name, 'A')
        for rdata in answers:
            print("IP address:", rdata.address)

        # Récupérer le titre de la page d'accueil du site Web
        url = "http://" + domain_name
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        print("Title of the homepage:", title)




        # Query Google search engine
        url = f"https://www.google.com/search?q={target}"
        response = requests.get(url)

        # Parse the HTML response
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract email addresses from search results
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        emails = re.findall(email_pattern, str(soup))

        # Extract subdomains from search results
        subdomain_pattern = r"([A-Za-z0-9]+\.)?[A-Za-z0-9]+\." + target.replace(".", "\.")
        subdomains = re.findall(subdomain_pattern, str(soup))

        # Output the results
        print("Email addresses:")
        for email in set(emails):
            print(email)

        print("Subdomains:")    
        for subdomain in set(subdomains):
            print(subdomain)
    except:
        print("error 404")
print("Good bye")