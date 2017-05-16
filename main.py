#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import telebot
import random
import urllib
import json
import threading
import time

counter = 0
hour = 60 * 60

def worker():
	while True:
		counter = 0
		time.sleep(hour)

def canSend():
	if counter <= 20:
		return True
	return False

thread = threading.Thread(target=worker)
thread.start()

bot = telebot.TeleBot("119720842:AAG__-LvMk0r0TACTRypwn_Te8OTprKa8SI")

keks = ['кек', 'кпек', 'КЕК', 'Кек', 'кееееееК', 'лол кек чебурек', 'ишак тебя метил', 'КПЕК']
ornul = ['как мразь', 'как тварь', 'как пидор', 'как шлеха', 'как алеша попович', 'как стерва']
reply = ['Вот ты мышь...', 'Уйди лофтер!', 'Ты надоел уже', 'Шо, дизайнер шоли?', 'Обкекался мразь', 'Тоби пизда', 'Вали пидор', 'Соси писос', 'Член не дорос кукарекать']
telki = ['Слишком много телок', 'Попробуй позже', 'Я отказываюсь выполнять твои команды']
error = ['Телок дудосят', 'Хватит фапать бро', 'Что то пошло не так', 'Алеша попвич занят с телками, попробуй позже', 'Азиатки кончились']
stikers = [
	'CAADAwADDwMAAt0NBwl-2xGCWqBcTAI', # pesiy kek
	'CAADAgADTQADZ0g6CQa56P8cfBcjAg', #spanch bob
]

@bot.message_handler(commands=['kek'])
def handle_start_help(message):
	bot.send_message(message.chat.id, keks[random.randint(0, 7)])

@bot.message_handler(commands=['or'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Ору "+ornul[random.randint(0, 5)])

@bot.message_handler(commands=['telki'])
def handle_start_help(message):
	global counter
	if canSend():
		try:
			data = urllib.urlopen('http://api.oboobs.ru/noise/1/').read()
			obj = json.loads(data)
			counter += 1
			for img in obj:
				bot.send_photo(message.chat.id, 'http://media.oboobs.ru/noise/' + str(img['id']) + '.jpg')
		except Exception:
			bot.send_message(message.chat.id, error[random.randint(0, 4)])
	else:
		bot.send_message(message.chat.id, telki[random.randint(0, 2)])


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	if random.randint(0, 1) == 1:
		bot.send_sticker(message.chat.id, stikers[random.randint(0, 1)])
	else:
	    bot.send_message(message.chat.id, reply[random.randint(0, 8)])

bot.polling()

