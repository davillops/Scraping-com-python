from cgitb import text
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()
html

type(html) # Verificando o tipo de dado
html = html.decode('utf-8') # Decodificando o codigo HTML para uma facil vizualização
type(html) # Verificando novamente e dessa vez uma string ao inves de bytes
html

# Eliminando os caracteres de tabulação, quebra de linha etc

html.split() # Transforma em um tipo de lista (onde tem espaços, ele quebra a linha), (array)

" ".join(html.split()) # JOIN adiciona entre os caracteres

" ".join(html.split()).replace('> <', '><') # REPLACE substitui caractere 'X' por 'Y'

def trata_html(input): # fazendo o tratamento do HTML
    return " ".join(input.split()).replace('> <', '><')

html = trata_html(html) # atribuindo o tratamento
html
# Adcionando Beautifulsoup 
soup = BeautifulSoup(html, 'html.parser')
soup

type(soup)

print(soup.prettify())
soup

# Consulta especifica
soup.img.attrs

soup.img.attrs.keys()     # Ver apenas as chaves usadas
soup.img.attrs.values()   # Ver apenas os valores dentro das chaves
soup.img['class']         # Ver um atributo especifico com dicionario
soup.img.get('src')       # Acessar um atributo especifico
soup.img.attrs['src']     # "[]" significa o uso do dicionario Python

# Utilizando formais mais faceis com Find() e Find_all()
soup.find('img') # encontra o primeiro dado

soup('img') # Busca geral para todos que a tag img 
soup.find_all('img') # retorna todos os valores com a tag img

soup.findAll('img', limit= 1)[0] # ou seja parametro limit para definir a quantidade de retorno
                                 # e "[]" para selecionar dentro do array qual dado eu quero, nesse caso é o primeiro
                                 # de 0 a 1
# Buscando uma lista de tags
soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5'])
soup.findAll('p', {"class":"txt-value"}) # todos os "p" com valores x
soup.findAll('p', text = "Belo Horizonte - MG")
soup.findAll('img', alt= "Foto")
for item in soup.findAll('img', alt= "Foto"): # puxando apenas os links das imagens com .get('src')
    print(item.get('src'))

soup.find_all(text = True)
soup.find('h1')
soup.find('p').find_parent('div')
soup.find('p').find_parents()