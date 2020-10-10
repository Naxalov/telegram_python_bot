from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import telegram

TOKEN = os.environ['TOKEN']
sticker_id = 'AgACAgIAAxkBAAICR1-BhdNuCnrC45xLHbJuv7sif1gsAAJNrzEbh8IJSAQPMhcKQq4xxSOlli4AAwEAAwIAA3gAA5dzAgABGwQ'
bot = telegram.Bot(TOKEN)
# file_photo = open('logo.png', 'rb')
# print(type(file_photo))
bot.sendPhoto(
    chat_id='86775091',
    sticker=sticker_id,
)
