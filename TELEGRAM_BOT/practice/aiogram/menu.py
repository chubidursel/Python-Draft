from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Main menu!')
#------main menu---------
btnRandom = KeyboardButton('random number')
btnOther = KeyboardButton('wanna see nudes?')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom,btnOther)

#------other menu---------
btnInfo = KeyboardButton('Info')
btnMoney = KeyboardButton("here")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo,btnMoney, btnMain)
