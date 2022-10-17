import requests
from bs4 import BeautifulSoup


city = input("Name ur city: ")
url = f"https://en.wikipedia.org/wiki/{city}"
#print(url)

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "lxml")
title = soup.title.text
print(title)


print("------MAIN INFO---------")


var = soup.find(class_="infobox-data").text
print("country: " + var)

ppl = soup.find(class_="infobox ib-settlement vcard").find_all("mergedrow")
print(ppl)
