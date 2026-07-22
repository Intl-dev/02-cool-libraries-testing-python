#the libraries
import sqlite3
from bs4 import BeautifulSoup
from curl_cffi import requests

#the web page I'll be using
url = "https://quotes.toscrape.com/"


connection = sqlite3.connect("quotes.db") #this creates the file where I will put the database
cursor = connection.cursor() #this makes it so we can use sql in the file we created

cursor.execute( #This creates a table in the database if it doesn't exist, and then creates a column for author and for the quote
    """ 
    CREATE TABLE IF NOT EXISTS quotesdb (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT NOT NULL,
        quote TEXT NOT NULL UNIQUE
    )
"""
)

response = requests.get(url, impersonate="chrome120") #this puts in the variable "response" the result of the request, and it used curl_cffi to make it like I'm not a bot, although the web page doesn't block me I think

if response.status_code == 200: #if the request is successful do:
    soup = BeautifulSoup(response.content, "html.parser") #this makes it so python understands HTML using beautiful soap
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes: #for every quote found in the web page do:
        text = quote.find("span", class_="text").text.strip() #"quote" is not really the text in the HTML, the text is inside a span so this looks for it inside quote
        author = quote.find("small", class_="author").text.strip() #author is also inside "quote" so it looks for it too

        cursor.execute( #this inserts the author and quote to the database, I needed some help doing the sql, so I don't know what some things do, but I understand what it does
            "INSERT OR IGNORE INTO quotesdb (author, quote) VALUES (?, ?)" , (author, text)
        )
    connection.commit() #this saves the data we got from the web page inside our database
    print("it worked I think, look the data base")
connection.close() #this closes the connection with the database I think, I was told it was useful, so I just put it in