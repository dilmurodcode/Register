import asyncio

from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
TOKEN = "7545897814:AAG5IjuEFYqWioKTvWzSIzYdFjlTFFaN9i0"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def catch_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ro'yxatdan o'tish")]
        ], resize_keyboard=True
    )

    full_name = message.from_user.full_name
    await message.answer(text=f'Assalomu alaykum yaqinlarim {full_name}', reply_markup=keyboard)


async def main():
    print('working')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
