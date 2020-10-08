from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hi(update, context):
    print(context.bot.getMe())
    # print(update.message.text)


updater = Updater('1324065101:AAFC8E5163G83YMG5MJ_X9ay1tvnmZ_6Mds')

updater.dispatcher.add_handler(MessageHandler(Filters.text, hi))

updater.start_polling()
updater.idle()
