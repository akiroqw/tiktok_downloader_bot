# tiktok_downloader_bot

This Telegram bot was created to download videos without a watermark. The bot is written in the Python programming language and uses the Telebot library to interact with the Telegram API.

## Installation
* Create a bot in Telegram using BotFather and copy the token.
* Go to the website my.telegram.org and get api_id and api_hash
* Clone repository
```
$ git clone https://github.com/akiroqw/TikTokDownloader.git
$ cd TikTokDownloaderBot
```
* Install the necessary libraries using the requirements.txt
```
$ pip install -r requirements.txt
```
* Create a file .env in the src folder where the token, api_hash and api_id will be located
```py
TOKEN = ""
API_ID = ""
API_HASH = ""
```
* or you can insert the token, api_hash, and api_id here(src/config.py):
```py
apiid = ""
apihash = ""
tokenbot = ""
```
* Run script
```
$ py src/main.py
```
## Usage

To download the video, send the bot a link to the video with a watermark. The bot will process the link and send the video to the user without a watermark.
The bot also has a `/start` command that greets the user.

## Restrictions

The bot only works with videos from tiktok, which are available for download without authorization and are not copyrighted. Also, the bot may have restrictions on downloading videos from some sites.

This Telegram bot can be useful for those who want to download videos without watermarks from TikTok. The bot does not have an interface, just send a link to a video with a watermark. And it will send the video without watermark.
