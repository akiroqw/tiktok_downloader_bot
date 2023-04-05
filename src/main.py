from config import *
from downloader import Downloader
from video import Video

bot = Bot(token=tokenbot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        await message.reply(f'Hello 👋🏻, {message.chat.first_name}! I can download videos from TikTok without a watermark. First of all, send me a link.\n')
    except Exception as ex:
        print(ex)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        if message.text.startswith('http') or message.text.__len__() > 0:

            video = Video(message.text, str(uuid.uuid4()), "mp4")
            dw = Downloader()
            dw.download_video(video.url, video.path)

            with open(video.path, 'rb') as vd:
                await bot.send_video(message.chat.id, vd)
        else:
            await bot.send_message(message.chat.id, "The link is incorrect.")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    print("The bot is running: " + "[" + str(datetime.datetime.now()) + "]")
    aiogram.executor.start_polling(dp, skip_updates=True)
