import requests
from bs4 import BeautifulSoup
import os

all_links = []
www = input("website: ")
try:
    response = requests.get(www)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    for link in links:
        all_links.append(link.get("href"))
    print(all_links)
    title = soup.find("title")
    # dump links into file with wegsite name
    with open(title.text + ".txt", "w") as f:
        for link in all_links:
            f.write(str(link + "\n"))
            
except Exception as e:
    print("Invalid website")
    print(e)