import aiogram
from aiogram import Bot, Dispatcher, types
import asyncio
from config import TOKEN
from aiogram.filters.command import Command
from aiogram.types.input_file import FSInputFile
from aiogram import F
from PIL import Image
import os

bot = Bot(TOKEN)
dp = Dispatcher()


# activate bot with instruction

@dp.message(Command('start'))
async def bot_start(message: types.Message):
    await message.answer("Hello, i can convert photo to tg's stiker format, let's go? Just send me a photo")


# bot will activate by sended photo, resize it to telegram sticker format
@dp.message(F.photo)
async def convert_photo_to_png_512_512(message: types.Message):
    await bot.download(message.photo[-1], destination="./photo.jpeg")

    image = Image.open('./photo.jpeg')
    new_image = image.resize((512, 512))
    new_image.save("./photo.png")
    os.remove("./photo.jpeg")
    file = FSInputFile("./photo.png")
    await bot.send_document(message.chat.id, document=file)
    os.remove('./photo.png')


# activate infinity polling
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
