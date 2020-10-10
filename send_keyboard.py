from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

import os

TOKEN = os.environ['TOKEN']


def hi(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, text)


def start(update, context):

    reply_markup = ReplyKeyboardMarkup(
        [
            ['Button1']
        ]
    )
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(
        chat_id=chat_id,
        text='Welcome to our bot',
        reply_markup=reply_markup
    )


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(Filters.text, hi))


updater.start_polling()
updater.idle()
