from config import *
from downloader import Downloader

bot = Bot(token=tokenbot)
dp = Dispatcher(bot)


@dp.message_handler()
async def handle_message(message: aiogram.types.Message):
    try:
        if message.text.startswith('http') and message.text.__len__() > 0:
            
            video_url = message.text
            video_name = str(uuid.uuid4())
            dw = Downloader()
            dw.download_video(video_url, video_name + ".mp4")

            with open(video_name + '.mp4', 'rb') as video:
                await bot.send_video(message.chat.id, video)
            
            os.remove(video_name + '.mp4')
        else:
            await bot.send_message(message.chat.id, "The link is incorrect.")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    print("The bot is running: " + "[" + str(datetime.datetime.now()) + "]")
    aiogram.executor.start_polling(dp, skip_updates=True)
