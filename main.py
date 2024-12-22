import ptbot


TG_TOKEN = '7482916524:AAEyJv3EDGGo2k3liTIGNoCF3r3C_nqrLtI'  # подставьте свой
TG_CHAT_ID = '650796925'  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)
bot.send_message(TG_CHAT_ID, "Бот запущен")