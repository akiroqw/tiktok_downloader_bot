from config import *
from downloader import Downloader

bot = Bot(token=tokenbot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        await message.reply(f'Welcome, {message.chat.first_name}!Send a link to the video.\n')
    except Exception as ex:
        print(ex)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        if message.text.startswith('http') or message.text.__len__() > 0:
            video = Video(message.text, "mp4")
            dw = Downloader()
            dw.download_video(video.url, video.path)
            await bot.send_video(message.chat.id, video.get_video())
        else:
            await bot.send_message(message.chat.id, "The link is incorrect.")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    print("The bot is running: " + "[" + str(datetime.datetime.now()) + "]")
    aiogram.executor.start_polling(dp, skip_updates=True)
