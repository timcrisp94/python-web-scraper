import requests
from bs4 import BeautifulSoup

URL = "https://www.cagematch.net/?id=1&nr=356506"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="Matches")

# print(results.prettify())