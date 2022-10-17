import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as bs
# https://pypi.org/project/pyTelegramBotAPI/

bot = telebot.TeleBot('5113509994:AAG2jQ-9mubMMpyRMUJgwLtO2Nvmx8zo8fc')

@bot.message_handler(commands=["start"])
def start(message): # "message" is what we recive from users
    mes = "Salam Aleikum!"
    bot.send_message(message.chat.id, mes)
    # 2 parameters (where we send message >> message.cad.id /// text **(also can use as HTML file) '<b>Salam</b>, parse_mode="html

@bot.message_handler(commands=['web'])
def web(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("XXX", url="https://pypi.org/project/pyTelegramBotAPI/"))
    bot.send_message(message.chat.id, "Wanna see boobs?", reply_markup=markup)

@bot.message_handler(commands=['key'])
def web(message):
    markup1 = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/web')
    itembtnv = types.KeyboardButton('pic')
    itembtnc = types.KeyboardButton('game')
    markup1.row(itembtna, itembtnv, itembtnc)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup1)

# --------------anegdot fun------------
URL = 'https://www.anekdot.ru/last/anekdot/'
def parser(url):
    res = requests.get(url)
    soup = bs(res.text, "html.parser")
    anegdot = soup.find_all('div', class_="text")
    return [c.text for c in anegdot]

list_of_jokes = parser(URL)


# function for telegram

@bot.message_handler(commands=['joke'])
def jokes(message):
    bot.send_message(message.chat.id,list_of_jokes[0])
    del list_of_jokes[0]


# get text what users typing into chat box
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Salam":
        bot.send_message(message.chat.id, "Baurim Khallaisn?")
    elif message.text == "all":
        bot.send_message(message.chat.id, message)
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id:{message.from_user.id}")
    elif message.text == "pic":
        photo = open("pic.png", 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "听不懂你的讲话")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Nice photo! \n send me ur tits now!")


print('Working')
bot.polling(none_stop=True) #constantly executing
