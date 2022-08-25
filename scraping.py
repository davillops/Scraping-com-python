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
html