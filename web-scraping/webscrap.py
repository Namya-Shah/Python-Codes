import requests
from bs4 import BeautifulSoup
import csv

site_to_scrape = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(site_to_scrape.text, 'html.parser')
quotes = soup.findAll("span", {'class': 'text'})
authors = soup.findAll("small", {'class': 'author'})

file = open("webscrape.csv", "w")
writer = csv.writer(file)

writer.writerow(["Quotes", "Author"])

for quote, author in zip(quotes, authors):
    print(quote.text, "-", author.text)
    writer.writerow([quote.text, author.text])

file.close()