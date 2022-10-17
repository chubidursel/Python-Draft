import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.central.co.th/en/tech/audio-hifi/headphones-earpieces"
HEADEERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

def get_html(url, params=''):
    r = requests.get(url=url, headers=HEADEERS,params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find(class_="_3hiFF _11_I2 PriceContainerView__StyledFinalPrice-sc-1abzx5y-2 gJXyDs _11_I2").find("data-testid").text

    card = []

    print(items)

html = get_html(url)
get_content(html)
