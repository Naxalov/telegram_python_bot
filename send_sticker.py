from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import telegram
from pprint import pprint
TOKEN = os.environ['TOKEN']
file_id_sticker = 'CAACAgIAAxkBAAICH1-BM7_EsqCc2nBSFjaDkpWoI6UsAAIUAANOXNIpeTENMSnHY0MbBA'

bot = telegram.Bot(TOKEN)

# file_sticker = open('logo.webp', 'rb')
# print(type(file_photo))
msg = bot.sendSticker(
    chat_id='86775091',
    sticker=file_id_sticker,
)
print(msg.sticker.file_id)
print(msg.sticker.file_unique_id)
