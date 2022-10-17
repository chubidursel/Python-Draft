import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hey, Whats uppp? Tell me the name of the city where u wanna check the weather: ")

@dp.message_handler()
async def get_weather(message: types.Message):

    code_to_smile = {
        "Clear": "Awesome \U0001F600",
        "Clouds": "Cloudy \U0001F601",
        "Rain": "Raining \U00002614",
        "Drizzle": "Drizzlee \U00002614",
        "Thunderstorm": "Thunder \U000026A1",
        "Snow": "Snowing \U0001F328",
        "Mist": "Mist \U0001F32B"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data['main']["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look outside, idk what's going on there! LOL"

        humidity = data["main"]["humidity"]
        wind = data['wind']["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f'weather in the city: {city}\n'
              f"temperature: {cur_weather} C° {wd}\n"
              f"humidity: {humidity}%\n"
              f"wind: {wind}M/S\n"
              f"Sunrise: {sunrise_timestamp}\n"
              f"Sunset: {sunset_timestamp}\n"
              f"Lenght of the day: {length_of_the_day}\n"
              f"***Have a good day!***")

    except:
        await message.reply("\U00002620 Check the name of the city \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)