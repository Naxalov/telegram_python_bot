from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import telegram

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(TOKEN)
bot.sendPhoto(
    chat_id='86775091',
    photo='https://random.dog/42e97d6a-c825-4191-9434-32cea191fc21.jpeg',
    caption='DOG'
)
