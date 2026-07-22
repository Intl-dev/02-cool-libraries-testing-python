import requests #the library to make http/https requests
from bs4 import BeautifulSoup #the library to scrape web pages

url = "https://books.toscrape.com/" #the web page I'll be using

response = requests.get(url) #this makes the request to the web page

if response.status_code == 200: #if the request is successful, then happens what is inside the if
    soup = BeautifulSoup(response.content, 'html.parser') #I think this makes it so python understands HTML
    products = soup.find_all('article', class_='product_pod') #this looks for every item that is <article> in the HTML and that has de class product pod
    for product in products: #for every product that is an <article> and has the class product pod do:
        product_price = product.find('div', class_='product_price') #this looks for the <div> with the class product price
        price = product_price.find('p', class_='price_color').text.strip() #this looks for the real division that has the price and takes the text with .text and eliminates the blank spaces with .strip()
        product_h3 = product.find('h3') #this looks for the division <h3> inside the product because inside it has the name of it
        name = product_h3.find('a')['title'] #this looks for the division, in this case <a> and inside it looks for 'title' because it contains the name of the product
        print(f"name: {name}, price: {price}") #prints the name and the price we got
