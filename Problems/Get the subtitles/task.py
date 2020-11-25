import requests

from bs4 import BeautifulSoup


n = int(input())
url = input()
r = requests.get(url)
bs = BeautifulSoup(r.content, "html.parser")
sub = bs.find_all("h2")
print(sub[n].text)
