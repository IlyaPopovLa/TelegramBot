import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def wait(bot, tg_chat_id, question):
    bot.send_message(tg_chat_id, "Бот запущен")
    time = parse(question)
    message_id = bot.send_message(tg_chat_id, "Таймер запущен на {} секунд\n{}".format(time, render_progressbar(time, 0)))
    bot.create_countdown(time, notify_progress, mid=message_id, timer=time, tg_chat_id=tg_chat_id)
    bot.create_timer(time, message_func, tg_chat_id=tg_chat_id)


def notify_progress(bot, tg_chat_id, secs_left, mid, timer):
    bot.update_message(tg_chat_id, mid, "Осталось {} секунд\n{}".format(secs_left, render_progressbar(timer, timer-secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def message_func(bot, tg_chat_id):
    bot.send_message(tg_chat_id, "Время вышло")


def main():
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")
    bot = ptbot.Bot(tg_token)
    bot.send_message(tg_chat_id, "На сколько запустить таймер?")
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == '__main__':
    main()