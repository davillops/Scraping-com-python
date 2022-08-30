from urllib import response
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# Declarando variavel card
cards = []
# Obtendo o HTML e o total de páginas
response = urlopen('https://alura-site-scraping.herokuapp.com/index.php?page=')
codigo = response.read().decode('utf-8')
soup = BeautifulSoup(codigo, 'html.parser')

pages = int(soup.find('span', class_='info-pages').get_text().split()[-1])
## Iterando por todas as páginas do site
for i in range(pages):
    ## Obtendo o HTML
    response = urlopen('https://alura-site-scraping.herokuapp.com/index.php?page=' + str(i + 1)) # +1 porque o indice começa no zero
    codigo = response.read().decode('utf-8')
    soup = BeautifulSoup(codigo, 'html.parser')

    # Obtendo as tags de interesse
    anuncios = soup.find('div', {'id':'container-cards'}).find_all('div', class_='card')

    # Coletando as informações dos CARDS
    for anuncio in anuncios:
        card = {}
        card['value'] = anuncio.find('p', {'class':'txt-value'}).get_text()

        infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
        for info in infos:
            card[info.get('class')[0].split('-')[-1]] = info.get_text()
        
        items = anuncio.find('ul', {'class':'lst-items'}).findAll('li')
        items.pop()
        
        for item in items:
            acessorios = []
            acessorios.append(item.getText().replace('►', ''))
        card['items'] = acessorios

    # Adicionando resultado a lista Cards
        cards.append(card) # colocando tudo dentro da lista cards
        image = anuncio.find('div', {'class':'image-card'}).find('img')
        urlretrieve(image.get('src'), './imagens/' + image.get('src').split('/')[-1])

# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset
dataset.to_csv('.\dataSet.csv', sep=';', index=False, encoding='utf-8-sig')

# Todas as paginas
soup.find('span', class_='info-pages').get_text().split()[-1] # string
int(soup.find('span', class_='info-pages').get_text().split()[-1]) # inteiro
