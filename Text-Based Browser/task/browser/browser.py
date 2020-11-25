from sys import argv
from os import mkdir
from os import path
from _collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore


def append_prev():
    global prev_page, stack
    if prev_page != "":
        stack.append(prev_page)


init()
tags = ["p", "a", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"]
stack = deque()
if len(argv) < 2:
    print("ERROR")
d_name = argv[1]
if not path.exists(d_name):
    mkdir(d_name)
prev_page = ""
while True:
    url = input()
    if url == "exit":
        break
    elif url == "back":
        if len(stack) == 0:
            continue
        else:
            with open(d_name + "/" + stack.pop(), "r") as f:
                print(f.read())
    else:
        file_path = d_name + "/" + url
        if path.exists(file_path):
            with open(file_path, "r") as f:
                for elem in f:
                    print(elem)
        else:
            is_url = url.find(".")
            if is_url != -1 and url[len(url) - 1] != ".":
                if "https://" in url:
                    r = requests.get(url)
                else:
                    r = requests.get("https://" + url)
                if not r:
                    print("Server not responding")
                    continue
                append_prev()
                name_file = url[:url.rfind(".")]
                prev_page = name_file
                bs = BeautifulSoup(r.content, "html.parser")
                elements = bs.find_all(tags)
                with open(d_name + "/" + name_file, "w") as f:
                    for elem in elements:
                        f.write(elem.text)
                        if elem.name == "a":
                            print(Fore.BLUE + elem.text)
                        else:
                            print(elem.text)
            else:
                print("Error: Incorrect URL")

