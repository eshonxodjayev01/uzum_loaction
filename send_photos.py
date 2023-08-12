from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.buy_books import book_keys
from loader import dp, bot


# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_file_id_p(message: types.Message):
#     await message.reply(message.photo[-1].file_id)
#
# @dp.message_handler(content_types=types.ContentType.VIDEO)
# async def get_file_id_v(message: types.Message):
#     await message.reply(message.video.file_id)

@dp.message_handler(Command("location"))
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAANnZMlFS3kMGDOXC9xXs6ZdgIbltw4AAozQMRuIi0hKSZzA6mD2TeEBAAMCAAN4AAMvBA"
    msg = "<b>Uzum Market</b> do'konlari.\n\n"
    msg += "<b>Eng yaqin Uzum Marketni toping📍:</b>\n\n\n👉📍 Eng yaqin do'konni topish ni tanlnag\n👉  Lokatsiyani yuboring!\n\n                        👇"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)