import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from googletrans import Translator

API_TOKEN = "8444512550:AAHn4ve81-Qjf2nPEBusBkizSZZEd-4uOR0"   # bu yerga tokeningizni yozing
TARGET_CHANNEL = "@rlfprouzb"         # bu yerga kanal username yozing

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def forward_and_translate(message: types.Message):
    text = ""
    if message.text:
        translated = translator.translate(message.text, dest="uz")  
        text = translated.text + "\n\n👉 " + TARGET_CHANNEL  

    if message.photo:
        await bot.send_photo(TARGET_CHANNEL, message.photo[-1].file_id, caption=text)
    elif message.video:
        await bot.send_video(TARGET_CHANNEL, message.video.file_id, caption=text)
    else:
        await bot.send_message(TARGET_CHANNEL, text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
