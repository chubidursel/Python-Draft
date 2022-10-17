import requests
from bs4 import BeautifulSoup

# !!!!! GET HTML + save !!!!!!!!!!!

# url = "https://www.sony.co.th/en/electronics/headphones/t/headband-headphones"
#
# HEADERS = {
#      "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
#  }
#
# req = requests.get(url, headers=HEADERS)
# src = req.text
# #print(src)
#
# with open("AAAindex.html", 'w', encoding="utf8") as file:
#     file.write(src)

# !!!!!!!!!! work with saved html file and EXTRACT smth !!!!!!!!
with open("AAAindex.html", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")

#dock = soup.prettify()
#print(dock)

#price_for_1 = soup.find("div", class_="product-price product-price--show").find("strong").text.strip()
#print(price_for_1)

# --------create cards of all products------------
cards = soup.find_all("div", class_="product-content mlp-block")
print(len(cards))

# --------collect all what we need from the cards------------
for item in cards:
    card_name = item.find("div", class_="product-name p2").find("strong").text
    #print(card_name)
    card_price = item.find("div", class_="product-price product-price--show").find("strong").text
    #print(card_price)
    print(f"{card_name} >>> {card_price}")



