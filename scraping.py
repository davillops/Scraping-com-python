from cgitb import html
from urllib import response
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html =  response.read()

soup = BeautifulSoup(html, 'html.parser')

print(soup.find('h1', id="hello-world").get_text())
print(soup.find('p').get_text())