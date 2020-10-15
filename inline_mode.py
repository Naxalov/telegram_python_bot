from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResult, InlineQueryResultArticle, InputTextMessageContent

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


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query

    msg = InputTextMessageContent(
        message_text='Text'

    )
    result1 = InlineQueryResultArticle(
        title='title 1',
        input_message_content=msg,
        thumb_url='https://freeiconshop.com/wp-content/uploads/edd/document-done-flat.png',

        id=1
    )
    results = [result1]
    print(query)
    update.inline_query.answer(results)

    # query = update.inline_query.query
    # results = [
    #     InlineQueryResultArticle(
    #         id=uuid4(), title="TEST 1", input_message_content=InputTextMessageContent('Answer from inline')
    #     )
    # ]

    # update.inline_query.answer(results)


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
    query.answer(
        text='😀 - Good\n😁Yaxshi\n😂Hello\n🤣 total',
        show_alert=True
    )


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(codeschool))
updater.dispatcher.add_handler(InlineQueryHandler(callback=inlinequery))

updater.start_polling()
updater.idle()
