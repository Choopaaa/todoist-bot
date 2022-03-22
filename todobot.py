from todoist import del_task
from todoist import add_task
from todoist import show_task
from telebot import types
import telebot

bot = telebot.TeleBot("5174519911:AAF16GH_61rLvmDcf4RQM4UWDKdGaQd_Q74", parse_mode=None)

@bot.message_handler(commands=['list'])
def send_welcome(message):
    bot.reply_to(message, "Вот список твоих задач", reply_markup = markup)

@bot.message_handler(func=lambda message: True)
def send_currency(message):
    if message.text == "Доллар":
        bot.reply_to(message, get_wallet("USDRUB"))
