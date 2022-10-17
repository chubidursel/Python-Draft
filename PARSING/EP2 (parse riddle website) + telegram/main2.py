import requests
from bs4 import BeautifulSoup
#IDK ho to finish this parser


url = 'https://www.riddles.com/'
req = requests.get(url)
html_file = req.text
#print(req.status_code)

soup = BeautifulSoup(html_file, 'lxml')
#print(soup.title.string)
riddle_cards = soup.find_all('div', class_="panel-body lead")
#print(riddle_cards)

for item in riddle_cards:
    each_riddle = soup.find('strong').next_element.next_element.text

    print(each_riddle)


