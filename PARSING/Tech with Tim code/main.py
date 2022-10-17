from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/corsair-16gb-288-pin-ddr4-sdram/p/N82E16820233859?Item=N82E16820233859&cm_sp=Homepage_SS-_-P1_20-233-859-_-04052022"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#dock = doc.prettify()
#print(dock)

prices = doc.find_all(text="$")
print(prices)
parent = prices[0].parent
print(parent)
strong = parent.find("strong")
print(strong.string)