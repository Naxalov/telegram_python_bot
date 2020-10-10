from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os


def hi(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, text)


def start(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Welcome to our bot')


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')


# updater = Updater('1324065101:AAFC8E5163G83YMG5MJ_X9ay1tvnmZ_6Mds')

# updater.dispatcher.add_handler(CommandHandler('help', help_bot))
# updater.dispatcher.add_handler(CommandHandler('start', start))

# updater.dispatcher.add_handler(MessageHandler(Filters.text, hi))


# updater.start_polling()
# updater.idle()

TOKEN = os.environ['TOKEN']
print(TOKEN)
