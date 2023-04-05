import datetime
import time
import uuid
import requests
import bs4
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import exceptions
import aiogram

load_dotenv()
apiid = os.environ.get("API_ID")
apihash = os.environ.get("API_HASH")
tokenbot = os.environ.get("TOKEN")




