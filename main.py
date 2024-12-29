import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")


def notify_progress(secs_left, time):
    bot.create_countdown(time, notify_progress)
    print("Осталось", secs_left)


def wait(chat_id, question):
    time = parse(question)
    bot.create_timer(time, choose, author_id=chat_id, message=question)


def choose(author_id, message):
    answers = ("Время вышло")
    bot.send_message(author_id, answers)
    print("Он спросил:", message)
    print("Я ответил:", answers)


bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(notify_progress)
bot.reply_on_message(wait)
bot.reply_on_message(choose)
bot.run_bot()