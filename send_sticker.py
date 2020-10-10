from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import telegram

TOKEN = os.environ['TOKEN']
file_id_sticker = 'CAACAgIAAxkBAAICH1-BM7_EsqCc2nBSFjaDkpWoI6UsAAIUAANOXNIpeTENMSnHY0MbBA'

bot = telegram.Bot(TOKEN)

# file_photo = open('logo.png', 'rb')
# print(type(file_photo))
bot.sendSticker(
    chat_id='86775091',
    sticker=sticker_id,
)
