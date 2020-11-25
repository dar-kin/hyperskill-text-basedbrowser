import requests

from bs4 import BeautifulSoup


url = input()
r = requests.get(url)
bs = BeautifulSoup(r.content, "html.parser")
inf = bs.find("h1")
print(inf.text)
