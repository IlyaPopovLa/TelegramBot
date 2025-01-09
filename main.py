import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse
load_dotenv()


TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
BOT = ptbot.Bot(TG_TOKEN)


def wait(TG_CHAT_ID, question):
    BOT.send_message(TG_CHAT_ID, "Бот запущен")
    time = parse(question)
    message_id = BOT.send_message(TG_CHAT_ID, "Таймер запущен на {} секунд\n{}".format(time, render_progressbar(time, 0)))
    BOT.create_countdown(time, notify_progress, mid=message_id, timer=time)
    BOT.create_timer(time, message_func)


def notify_progress(secs_left, mid, timer):
    BOT.update_message(TG_CHAT_ID, mid, "Осталось {} секунд\n{}".format(secs_left, render_progressbar(timer, timer-secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def message_func():
    BOT.send_message(TG_CHAT_ID, "Время вышло")


def main():
    BOT.send_message(TG_CHAT_ID, "На сколько запустить таймер?")
    BOT.reply_on_message(wait)
    BOT.run_bot()


if __name__ == '__main__':
    main()