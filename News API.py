import requests
import json
# from bs4 import BeautifulSoup

query = input("What kind of news you want to know ?\n")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-04-22&sortBy=publishedAt&apiKey=2e47c23efccd49b0957aa34df6e096b3"

r=requests.get(url)
# soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
news=json.loads(r.text)
# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------")