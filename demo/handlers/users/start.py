from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,db,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await db.add_user(full_name=message.from_user.full_name,user_id=message.from_user.id)
    except:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!")