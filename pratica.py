from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://alura-site-scraping.herokuapp.com/index.php'
resp = urlopen(url)
codig = resp.read().decode('utf-8')

sopinha = BeautifulSoup(codig, 'html.parser')

cards = []
card= {}
#
anuncio = sopinha.find('div', {"class":"well card"})

anuncio.find('div', {"class":"value-card"})
anuncio.find('p', {"class":"txt-value"}).get_text() # pega o valor do carro
card['value'] = anuncio.find('p', {"class":"txt-value"}).get_text() # colocando o valor dentro do card
# 
# card.update['value'] = anuncio.find('p', {"class":"txt-value"}).get_text() # atualizando o dicionario
#
anuncio.find('div', {'class':'body-card'}).findAll('p')

infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
#for info in infos:
#    print(info)
#for info in infos:
#    print(info.get('class'), ' - ', info.get_text())
#for info in infos:
#    print(info.get('class')[0], ' - ', info.get_text()) 
#for info in infos:
#    print(info.get('class')[0].split('-')[-1], ' - ', info.get_text()) #[-1] menos a primeira palavra de cada linha
for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text()

anuncio.find('ul', {'class':'lst-items'}).findAll('li')
items = anuncio.find('ul', {'class':'lst-items'}).findAll('li')
items.pop() # removo o ultimo item da lista
for item in items:
    print(item.getText())
for item in items:
    print(item.getText().replace('►', ''))

acessorios = []

for item in items:
    acessorios.append(item.getText().replace('►', '')) # append, cria a lista e joga p dentro os dados
card['items'] = acessorios

dataset = pd.DataFrame(card)
dataset = pd.DataFrame.from_dict(card, orient= 'index') # ajustando para o dataframe ficar correto
dataset

dataset = pd.DataFrame.from_dict(card, orient= 'index').T # voltar ao normal
dataset
# T -> transpor ou seja de linha para coluna ou ao contrario
# criando arquivo csv
dataset.to_csv('.\dataSet.csv', sep=';', index=False, encoding='utf-8-sig')

anuncio.find("div", {"class":"imagem-card"})

image = anuncio.find('div', {'class':'image-card'}).find('img')
image.get('src')
print(image.get('src'))
image.get('src').split('/')[-1]
urlretrieve(image.get('src'), './imagens/' + image.get('src').split('/')[-1])

# GERAL #

len(sopinha.find('div', {'id':'container-cards'}).findAll('div', class_="card"))
# len = contar quantos itens tem na lista, ou seja quantas 'div'
sopinha.find('div', {'id':'container-cards'}).find_all('div', class_='card')
anuncios = sopinha.find('div', {'id':'container-cards'}).findAll('div', class_='card')

# for ITEM IN ITENS

for anuncio in anuncios:
    print(str(anuncio)+"\n\n") # \n significa espaço (pular)

# Valor
card['value'] = anuncio.find('p', {"class":"txt-value"}).get_text()

# Informações
infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
for info in infos:
  card[info.get('class')[0].split('-')[-1]] = info.get_text()

# Acessorios
items = anuncio.find('ul', {'class':'lst-items'}).findAll('li')
items.pop()
acessorios = []
for item in items:
  acessorios.append(item.getText().replace('►', ''))
card['items'] = acessorios

# Imagens
image = anuncio.find('div', {'class':'image-card'}).find('img')
urlretrieve(image.get('src'), './imagens/' + image.get('src').split('/')[-1])
