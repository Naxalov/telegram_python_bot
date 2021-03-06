from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

import os

TOKEN = os.environ['TOKEN']


def hi(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, text)


def start(update, context):
    button = KeyboardButton(
        text='contact',
        request_contact=True
    )
    reply_markup = ReplyKeyboardMarkup(
        [
            [button]
        ]
    )
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(
        chat_id=chat_id,
        text='Share your Contact Phone',
        reply_markup=reply_markup
    )


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')


def get_contact(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    contact = update.message.contact
    phone = contact.phone_number
    firsr_name = contact.first_name
    last_name = contact.last_name
    txt = f'Phone:{phone}\nFirst name:{firsr_name}\nLast Name:{last_name}'
    print(txt)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))


updater.dispatcher.add_handler(MessageHandler(Filters.text, hi))
updater.dispatcher.add_handler(
    MessageHandler(Filters.contact,
                   get_contact))

updater.start_polling()
updater.idle()
