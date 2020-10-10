import telegram
from pprint import pprint
bot = telegram.Bot(token='1324065101:AAFC8E5163G83YMG5MJ_X9ay1tvnmZ_6Mds')
# bot.sendPhoto(chat_id='86775091',
#               photo='https://open.coop/wp-content/uploads/2020/04/telegram-logo.png')
user = bot.getMe()
update = bot.getUpdates()[0]
# print(user)
print(update)
