import requests
from bs4 import BeautifulSoup as bs
import random
import telebot

URL = 'https://www.anekdot.ru/last/anekdot/'
def parser(url):
    res = requests.get(url)
    soup = bs(res.text, "html.parser")
    anegdot = soup.find_all('div', class_="text")
    return [c.text for c in anegdot] #create a list of jokes

list_of_jokes = parser(URL)
print(list_of_jokes[2])
#del list_of_jokes[0]

x = int(input("Chose the number: "))
print(list_of_jokes[x])





# function for telegram
'''''
@bot.message_handler(command='joke')
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id,list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Chose the number, please')
'''''