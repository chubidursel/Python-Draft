from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav
from pycoingecko import CoinGeckoAPI
import random


# Initialize bot and dispatcher
bot = Bot(token='5247406807:AAEoB18tjkIB5jjYc96uSxuvkm3bj_nLO44')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salam! {message.from_user.first_name}\nI'm the best Bot in Telegram!\nPowered by aiogram.")

#-----------CRYPTO!---------
cg = CoinGeckoAPI()
@dp.message_handler(commands=['crypto'])
async def send_welcome(message: types.Message):
    await message.answer("What do u want to check?: ", reply_markup=nav.crypto_list)
@dp.callback_query_handler(text_contains = "cc_")
async def crupto(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    currency = str(callback_data[3:])
    result = cg.get_price(ids=currency, vs_currencies='usd')
    await bot.send_message(call.from_user.id, f"crypto: {currency}\nprice: {result[currency]['usd']}$", reply_markup=nav.crypto_list)

#-----------MENU--(functioun in main message handler below)-----
import menu as mmm
@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    await message.answer("Whats upppp?", reply_markup=mmm.mainMenu)


#----------------DICE GAME----------------------------
from asyncio import sleep
@dp.message_handler(commands=['play'])
async def send_welcome(message: types.Message):
    await message.answer("Heyyy gambler!\nWanna lose ur last coin?\nLet's play dice!")
    await sleep(1)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(4)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, "Hahaha, LOOOSER!")
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, "Luckyyy dudeee!")
    else:
        await bot.send_message(message.from_user.id, "Tie! =(")


#--------------MAIN message handler------------
@dp.message_handler()
async def echo_send(message: types.Message):
    #chatID = message.chat.id
    #text = f"Salam{message.from_user.first_name}"
    if message.text.lower() == "salam":
        await message.answer("Baurim Khalaisin?")
#--------menu-------
    elif message.text == 'random number':
        await message.answer("Your number is >>> " + str(random.randint(1,100)))
    elif message.text == 'wanna see nudes?':
        await message.answer("Other", reply_markup=mmm.otherMenu)
    elif message.text == 'here':
        photo = open("photo.jpg", 'rb')
        await message.answer_photo(photo)
    elif message.text == 'Main menu!':
        await message.answer("Welcome back!", reply_markup=mmm.mainMenu)
    elif message.text == 'Info':
        await message.answer("This command is empty, u can add another function!")


# ---- rest-------------
    elif message.text.lower() == "all":
        await message.answer(message)
    elif message.text.lower() == "web":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("XXX", url="https://docs.aiogram.dev/en/latest/quick_start.html"))
        await message.answer("Wanna see boobs?", reply_markup=markup)
    else:
        await message.reply("I dont understand!\n Чё блять?\n听不懂你的讲话\nฉันไม่เข้าใจ!")


#executing our t-bot
executor.start_polling(dp, skip_updates=True)

# skip_updates=True >> if bot is offline and comes back online it won't read any messanges