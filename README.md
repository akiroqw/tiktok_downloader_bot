# TikTokDownloader

This Telegram bot was created to download videos without a watermark. The bot is written in the Python programming language and uses the Telebot library to interact with the Telegram API.

## Installation
1. Create a bot in Telegram using BotFather and copy the token.
2. Go to the website my.telegram.org and get api_id and api_hash
3. Clone repository
```
$ git clone https://github.com/akiroqw/TikTokDownloader.git
$ cd TikTokDownloaderBot
```
2. Install the necessary libraries using the requirements.txt
```
  $ pip install -r requirements.txt
```
3. Create a file .env in the src folder where the token, api_hash and api_id will be located
```py
TOKEN = ""
API_ID = ""
API_HASH = ""
```
4. Run script
```
$ py src/main.py
```
