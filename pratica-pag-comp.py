from distutils.filelist import findall
from os import sep
from urllib import response
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# Declarando variavel card
cards = []
# Obtendo o HTML
response = urlopen('https://alura-site-scraping.herokuapp.com/')
codigo = response.read().decode('utf-8')
sopinha = BeautifulSoup(codigo, 'html.parser')

# Obtendo as tags de interesse
anuncios = sopinha.find('div', {'id':'container-cards'}).find_all('div', class_='card')
# Coletando as informações dos CARDS
acessorios = []
for anuncio in anuncios:
    card = {}
    card['value'] = anuncio.find('p', {'class':'txt-value'}).get_text()

    infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
    for info in infos:
        card[info.get('class')[0].split('-')[-1]] = info.get_text()
    
    items = anuncio.find('ul', {'class':'lst-items'}).findAll('li')
    items.pop()
    
    for item in items:
        acessorios.append(item.getText().replace('►', ''))
    card['items'] = acessorios

# Adicionando resultado a lista Cards
    cards.append(card) # colocando tudo dentro da lista cards

    image = anuncio.find('div', {'class':'image-card'}).find('img')
    urlretrieve(image.get('src'), './imagens/' + image.get('src').split('/')[-1])

# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset.to_csv('.\dataSet.csv', sep=';', index=False, encoding='utf-8-sig')