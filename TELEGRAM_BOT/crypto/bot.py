from aiogram import Bot, executor, Dispatcher, types
from config import cfg
import markups as nav
from pycoingecko import CoinGeckoAPI

bot = Bot(token=cfg)
dp = Dispatcher(bot)
cg = CoinGeckoAPI()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Choose crypto: ", reply_markup=nav.crypto_list)

#find any crypto by message
@dp.message_handler()
async def bot_message(message: types.Message):
    result = cg.get_price(ids=message.text, vs_currencies='usd')
    await bot.send_message(message.from_user.id, f"crypto: {message.text}\nprice: {result[message.text]['usd']}$")


@dp.callback_query_handler(text_contains = "cc_")
async def crupto(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    currency = str(callback_data[3:])
    result = cg.get_price(ids=currency, vs_currencies='usd')
    await bot.send_message(call.from_user.id, f"crypto: {currency}\nprice: {result[currency]['usd']}$", reply_markup=nav.crypto_list)




if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)