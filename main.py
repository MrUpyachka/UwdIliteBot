#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import telebot
import random
import urllib
import json

bot = telebot.TeleBot("119720842:AAG__-LvMk0r0TACTRypwn_Te8OTprKa8SI")

keks = ['кек', 'кпек', 'КЕК', 'Кек', 'кееееееК', 'лол кек чебурек', 'ишак тебя метил', 'КПЕК']
ornul = ['как мразь', 'как тварь', 'как пидор', 'как шлеха', 'как алеша попович', 'как стерва']

@bot.message_handler(commands=['kek'])
def handle_start_help(message):
	bot.send_message(message.chat.id, keks[random.randint(0, 7)])

@bot.message_handler(commands=['or'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Ору "+ornul[random.randint(0, 5)])

@bot.message_handler(commands=['telki'])
def handle_start_help(message):
	try:
		data = urllib.urlopen('http://api.oboobs.ru/noise/1/').read()
		obj = json.loads(data)
		for img in obj:
			bot.send_message(message.chat.id, 'http://media.oboobs.ru/'+img['preview'])
	except Exception:
		bot.send_message(message.chat.id, 'Что то пошло не так...')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, 'Вот ты мышь....')

bot.polling()

