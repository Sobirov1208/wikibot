import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
API_TOKEN = '5044055234:AAHswCXJWpm7_O-AR5w-aeYQnXu6JYfcv84'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang("uz")
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"<b>Assalomu Alaykum {message.from_user.username} </b>",parse_mode="HTML")



@dp.message_handler()
async def WikiInfo(message: types.Message):
	try:
    	natija = wikipedia.summary(message.text)
    	await message.answer(natija)
    except:
    	await message.answer("Bunday maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)