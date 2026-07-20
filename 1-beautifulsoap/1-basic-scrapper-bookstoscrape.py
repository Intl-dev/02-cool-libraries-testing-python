import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('article', class_='product_pod')
    for product in products:
        product_price = product.find('div', class_='product_price')
        price = product_price.find('p', class_='price_color').text.strip()
        product_h3 = product.find('h3')
        name = product_h3.find('a')['title']
        print(f"name: {name}, price: {price}")
