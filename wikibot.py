
import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
from Button import *

from aiogram.types import Message, CallbackQuery


API_TOKEN = '5022604793:AAGW2cTVL8SK4s4XlrdQpZgQLV5rVqLoIHQ'



logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang("uz")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('tilni tanlang / choose language', reply_markup=til)


@dp.message_handler(text="uz O'zbekcha")
async def uzbekcha_uchun(message: types.Message):
    await message.answer("Assalomu Alaykum Botimizga Xush Kelibsiz!",reply_markup=uzbek)


@dp.message_handler(text="ru Русский")
async def ruscha_uchun(message: types.Message):
    await message.answer("privet!",reply_markup=ruscha)


@dp.callback_query_handler(text="info")
async def inline_tugma_uchun(call: CallbackQuery):
    await call.message.answer("Botimiz test uchun yaratildi")


@dp.callback_query_handler(text="aloqa")
async def inline_tugma_uchun(call: CallbackQuery):
    await call.message.answer("Aloqa uchun adminlarni tanlang:",reply_markup=admin)


@dp.callback_query_handler(text="инфо")
async def inline_tugma_uchun(call: CallbackQuery):
    await call.message.answer("Botimiz test uchun yaratildi")


@dp.callback_query_handler(text="admin1")
async def inline_tugma_uchun(call: CallbackQuery):
    await call.message.answer("993323")


@dp.callback_query_handler(text="admin2")
async def inline_tugma_uchun(call: CallbackQuery):
    await call.message.answer("972992")



@dp.callback_query_handler(text="связь")
async def inline_tugma_uchun(call: CallbackQuery):
    await call.message.answer("Aloqa yaxshi emas")

@dp.message_handler()
async def WikiInfo(message: types.Message):
	try:
		natija = wikipedia.summary(message.text)
		await message.answer(natija)
	except:
		await message.answer("Bunday maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)