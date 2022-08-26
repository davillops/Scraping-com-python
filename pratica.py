from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'
resp = urlopen(url)
codig = resp.read().decode('utf-8')

sopinha = BeautifulSoup(codig, 'html.parser')

cards = []
card= {}

anuncio = sopinha.find('div', {"class":"well card"})
anuncio.find('div', {"class":"value-card"})
anuncio.find('p', {"class":"txt-value"}).get_text()
card['value'] = anuncio.find('p', {"class":"txt-value"}).get_text() # colocando o valor dentro do card
card

# RESUMO
card['value'] = anuncio.find('p', {"class":"txt-value"}).get_text()