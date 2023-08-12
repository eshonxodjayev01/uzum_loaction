from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command

from keyboards.inline.buy_books import book_keys
from loader import dp

@dp.message_handler(CommandStart())
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAANnZMlFS3kMGDOXC9xXs6ZdgIbltw4AAozQMRuIi0hKSZzA6mD2TeEBAAMCAAN4AAMvBA"
    msg = "<b>Uzum Market</b> do'konlari.\n\n"
    msg += "<b>Eng yaqin Uzum Marketni toping📍:</b>\n\n\n👉📍 Eng yaqin do'konni topish ni tanlnag\n👉  Lokatsiyani yuboring!\n\n                        👇"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!\n\n<b>Foydalanish uchun:</b>\n\n/location buyrug'ini jo'nating")
