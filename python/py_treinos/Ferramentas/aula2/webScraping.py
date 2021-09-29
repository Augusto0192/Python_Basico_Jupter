from bs4 import BeautifulSoup
import requests

site = requests.get("https://novelmania.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())