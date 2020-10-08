from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hi(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, text)


updater = Updater('1324065101:AAFC8E5163G83YMG5MJ_X9ay1tvnmZ_6Mds')

updater.dispatcher.add_handler(MessageHandler(Filters.text, hi))

updater.start_polling()
updater.idle()
