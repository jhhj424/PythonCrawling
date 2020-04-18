import telegram

my_token = '839037088:AAG_AJZ5iQXsMSDgXtFIagWxdHRbbhkbUF8'
bot = telegram.Bot(token = my_token)
bot.sendMessage(chat_id=824661375, text='테스트입니다.')