from urllib.request import urlopen
from bs4 import BeautifulSoup

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

# RESUMO
# card['value'] = anuncio.find('p', {"class":"txt-value"}).get_text()
# infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
# for info in infos:
#   card[info.get('class')[0].split('-')[-1]] = info.get_text()