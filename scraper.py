from bs4 import BeautifulSoup
import requests
import ast
import pandas as pd

products = []
for i in range(31):
    url = f'https://www.jumbo.com/producten/categorieen/wijn,-bier,-sterke-drank/bier---speciaalbier/?PageNumber={i}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    html = result.content.decode()

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="jum-item jum-item-product ")
    for item in items:
        product = ast.literal_eval(item['data-jum-product-details'])
        products.append(product)
df = pd.DataFrame(products)
df.to_csv('jumbo_beer.csv')
