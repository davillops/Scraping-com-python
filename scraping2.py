from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read().decode('utf8')

soup = BeautifulSoup(html, 'html.parser')
soup
def trata_html(input):
    return " ".join(input.split()).replace('> <', '><')
soup = trata_html(soup)
soup.find('h1').find_next()

soup.find_all('img')
for item in soup.find_all('img'):
    print(item.get('src'))
soup.find('a')
soup.findAll('a')
soup.findAll('div', {"class":"container"})
