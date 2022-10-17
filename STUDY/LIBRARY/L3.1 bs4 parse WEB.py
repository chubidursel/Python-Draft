from bs4 import BeautifulSoup
import requests

# 1 STEP >> Extract the HTML content using the requests library.
# 2 STEP >> Analyze the HTML structure and identify the tags which have our content.
# 3 STEP >> Extract the tags using Beautiful Soup and put the data in a Python list.

#We can get the HTML content from this WEBpage using requests:
url = 'https://coinmarketcap.com/currencies/bitcoin/'
response = requests.get(url)
html = response.text

# ------------  Put HTML text into BS tree ------------
soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify()) # can print out the HTML content of the page, formatted nicely, using the prettify method on the BS object.

# ----------------- Extracting content from the HTML ------------
var = soup.find(class_="priceValue").find("span").text

while True:
    def price():
        print(var)

    answer = input("Wanna see the price?: ")
    if answer == "no":
        print("So fck off!")
        break
    else:
        price()
