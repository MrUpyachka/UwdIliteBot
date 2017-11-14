#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import telebot
import random
import urllib
import json

bot = telebot.TeleBot("119720842:AAG__-LvMk0r0TACTRypwn_Te8OTprKa8SI")

keks = ['кек', 'кпек', 'КЕК', 'Кек', 'кееееееК', 'лол кек чебурек', 'ишак тебя метил', 'КПЕК']
ornul = ['как мразь', 'как тварь', 'как пидор', 'как шлеха', 'как алеша попович', 'как стерва', 'как орало', 'как орк',
         'как сосеска', 'как барбареска']
reply = ['Вот ты мышь...', 'Уйди лофтер!', 'Ты надоел уже', 'Шо, дизайнер шоли?', 'Обкекался мразь', 'Тоби пизда',
         'Вали пидор', 'Соси писос', 'Член не дорос кукарекать']
telki = ['Слишком много телок', 'Попробуй позже', 'Я отказываюсь выполнять твои команды']
error = ['Телок дудосят', 'Хватит фапать бро', 'Что то пошло не так', 'Алеша попвич занят с телками, попробуй позже',
         'Азиатки кончились']
stikers = [
    'CAADAwADDwMAAt0NBwl-2xGCWqBcTAI',  # pesiy kek
    'CAADAgADRwYAAkxb1gn9h6PpAyEkggI',  # optimus fuck
    'CAADAgADngADk8vUCDsXkJ5Ka6VsAg',
    'CAADAgADIwADTFvWCfkn7nruQyHoAg',
    'CAADAgAD6gEAAsE8ngaA44zCtd3nBAI',
    'CAADAgADTQADZ0g6CQa56P8cfBcjAg',  # spanch bob
]


@bot.message_handler(commands=['kek'])
def handle_start_help(message):
    bot.send_message(message.chat.id, keks[random.randint(0, len(keks) - 1)])


@bot.message_handler(commands=['or'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Ору " + ornul[random.randint(0, len(ornul) - 1)])


@bot.message_handler(commands=['info'])
def sendInfo(message):
    bot.send_message(message.chat.id,
                     "Жду пул реквесты тут (и звездочки тоже) -> https://github.com/LikiPiki/UwdIliteBot")


@bot.message_handler(commands=['telki'])
def handle_start_help(message):
    try:
        data = urllib.urlopen('http://api.oboobs.ru/noise/1/').read()
        obj = json.loads(data)
        for img in obj:
            bot.send_photo(message.chat.id, 'http://media.oboobs.ru/noise/' + str(img['id']) + '.jpg')
    except Exception:
        bot.send_message(message.chat.id, error[random.randint(0, 4)])


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if random.randint(0, 1) == 1:
        bot.send_sticker(message.chat.id, stikers[random.randint(0, len(stikers) - 1)])
    else:
        bot.send_message(message.chat.id, reply[random.randint(0, len(reply) - 1)])


bot.polling()
