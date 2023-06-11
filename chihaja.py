import requests
from bs4 import BeautifulSoup

# Fonction pour récupérer les informations d'un site web donné
def get_site_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    meta_tags = soup.find_all('meta')
    meta_descriptions = [tag.get('content', '') for tag in meta_tags if tag.get('name') == 'description']
    return {'title': title, 'meta_descriptions': meta_descriptions}

# Exemple d'utilisation de la fonction get_site_info
site_url = 'https://www.example.com'
site_info = get_site_info(site_url)
print(f"Titre du site : {site_info['title']}")
print(f"Description du site : {site_info['meta_descriptions']}")


# Fonction pour rechercher des informations sur un utilisateur sur les réseaux sociaux
def search_social_media(username):
    social_media_sites = ['https://www.facebook.com/', 'https://www.twitter.com/', 'https://www.linkedin.com/']
    results = {}
    for site in social_media_sites:
        url = site + username
        response = requests.get(url)
        if response.status_code == 200:
            results[site] = 'trouvé'
        else:
            results[site] = 'non trouvé'
    return results

# Exemple d'utilisation de la fonction search_social_media
username = 'john.doe'
social_media_results = search_social_media(username)
for site, status in social_media_results.items():
    print(f"{site} : {status}")
