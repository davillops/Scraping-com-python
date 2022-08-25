from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

soup.find('h1', {'class': 'sub-header'}).get_text()