from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

TOKEN = os.environ['TOKEN']


def start(update, context):

    button = InlineKeyboardButton(
        text='CodeSchoolUz',
        callback_data=345
    )

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button]
        ]
    )
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(
        chat_id=chat_id,
        text='Our Telegram Channel',
        reply_markup=reply_markup
    )


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')


def codeschool(update, context):
    query = update.callback_query
    data = query.data
    query.answer('GOOD!')
    print(data)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(codeschool))

updater.start_polling()
updater.idle()
