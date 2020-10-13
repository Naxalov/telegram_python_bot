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
        text='New Text: 0',
        reply_markup=reply_markup
    )


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')


def codeschool(update, context):

    button = InlineKeyboardButton(
        text='CodeSchoolUz',
        callback_data=345
    )

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button]
        ]
    )

    query = update.callback_query
    text = query.message.text
    count = ''
    for i in text:
        if i.isdigit():
            count += i

    count = int(count)
    count += 1
    print(count)
    query.edit_message_text(f'New Text:{count}', reply_markup=reply_markup)
    data = query.data
    query.answer('GOOD!')


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(codeschool))

updater.start_polling()
updater.idle()
