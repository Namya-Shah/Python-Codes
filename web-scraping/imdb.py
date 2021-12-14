import requests
from bs4 import BeautifulSoup
import csv

movie_scrape = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
soup = BeautifulSoup(movie_scrape.text, 'html.parser')
movie_names = soup.findAll("td", {"class": "titleColumn"})
imdb_ratings = soup.findAll("td", {"class": "ratingColumn imdbRating"})

file = open("Top Movies.csv", "w")
writer = csv.writer(file)

writer.writerow(["Movies", "IMDB Rating"])

for movie_name, imdb_rating in zip(movie_names, imdb_ratings):
    writer.writerow([movie_names.text, imdb_rating.text])

file.close()