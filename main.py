from bs4 import BeautifulSoup
import requests

barcode = input('Digite o código de barras:')
# Site que será coletado
site = f"https://go-upc.com/search?q={barcode.strip()}"

# Coleta os dados do site
html = requests.get(site).content

# Formatando os dados
dados = BeautifulSoup(html, 'html.parser')

title = dados.find("h1", class_="product-name")

print(f'{title.text}')
