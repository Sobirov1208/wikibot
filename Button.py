from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

til = ReplyKeyboardMarkup(
	keyboard = [
		[
		KeyboardButton(text="uz O'zbekcha"),
		KeyboardButton(text="ru Русский"),
		]
	],
	resize_keyboard=True
)


uzbek = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Info", callback_data="info"),
			InlineKeyboardButton("Aloqa", callback_data="aloqa"),

		],
	]
)



ruscha = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("инфо", callback_data="инфо"),
			InlineKeyboardButton("связь", callback_data="связь"),

		],
	]
)

admin = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("admin1", callback_data="admin1"),
			InlineKeyboardButton("admin2", callback_data="admin2"),

		],
	]
)
