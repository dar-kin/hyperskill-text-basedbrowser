import requests

from bs4 import BeautifulSoup


word = input()
url = input()

r = requests.get(url)
bs = BeautifulSoup(r.content, "html.parser")
par = bs.find_all("p")
for elem in par:
    if word in elem.text:
        print(elem.text)
        break
