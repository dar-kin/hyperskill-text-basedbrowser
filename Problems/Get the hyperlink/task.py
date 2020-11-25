import requests

from bs4 import BeautifulSoup


n = int(input())
url = input()
r = requests.get(url)
bs = BeautifulSoup(r.content, "html.parser")
links = bs.find_all("a")
print(links[n - 1].get("href"))
