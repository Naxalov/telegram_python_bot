from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hello(update, context):
    update.message.reply_text('Hello World')


updater = Updater(
    '1324065101:AAFC8E5163G83YMG5MJ_X9ay1tvnmZ_6Mds', use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.text, hello))

updater.start_polling()
updater.idle()
