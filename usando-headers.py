from urllib import response
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.alura.com.br'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'} # Necessario colocar o dicionario de python para acessar algumas paginas

try: # irá tentar executar o programa
    req = Request(url, headers= headers)
    response = urlopen(req)
    html = response.read()
    print(html)

except HTTPError as e: # caso a parte de cima de erro ira printar na tela o codigo do erro
    print(e.status, e.reason)
except URLError as e: # URLerror não mostra os status
    print(e.reason)   # Necessario ser nesta ordem para mostrar os erros de acord
