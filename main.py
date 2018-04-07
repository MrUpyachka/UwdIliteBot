#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import telebot
import random
import urllib
import json
import datetime

bot = telebot.TeleBot("119720842:AAG__-LvMk0r0TACTRypwn_Te8OTprKa8SI")
time = int(datetime.datetime.now().strftime("%H"))
bot_details = bot.get_me()
mentioned_key = '@' + bot_details.username

keks = ['кек', 'кпек', 'КЕК', 'Кек', 'кееееееК', 'лол кек чебурек', 'ишак тебя метил', 'КПЕК']
ornul = ['как мразь', 'как тварь', 'как пидор', 'как шлеха', 'как алеша попович', 'как стерва', 'как орало', 'как орк',
         'как сосеска', 'как барбареска']
reply = ['Вот ты мышь...', 'Уйди лофтер!', 'Ты надоел уже', 'Шо, дизайнер шоли?', 'Обкекался мразь', 'Тоби пизда',
         'Вали пидор', 'Соси писос', 'Член не дорос кукарекать']
telki = ['Слишком много телок', 'Попробуй позже', 'Я отказываюсь выполнять твои команды']
telki_ne_daut = ['Иди работай!', 'Телки только после работы', 'Ну не в рабочее время же!',
                 'Ты хочешь чтобы твои коллеги спалили тебя за телками? Я тоже нет', 'Кончится работа, начнутся телки!',
                 'Не в этот час', 'Трудовые будни, не до телок']
error = ['Телок дудосят', 'Хватит фапать бро', 'Что то пошло не так', 'Алеша попвич занят с телками, попробуй позже',
         'Азиатки кончились']
stikers = []
fuck_you_stickers = []


def extract_stickers_set(stickers_config_json, set_name):
    """Loads sticker ID's for specified set-name from config"""
    stickers = []
    for sticker in stickers_config_json[set_name]:
        stickers.append(sticker['file_id'])
    return stickers


def update_stickers_set(set_collection, actual_stickers_set):
    """Resets existing stickers collection and fills it with new stickers"""
    set_collection.clear()
    set_collection.extend(actual_stickers_set)


def load_stickers_config():
    """Loads all stickers sets"""
    stickers_config = ''.join(open('./stickers.json', 'r', encoding='utf-8').readlines())
    stickers_config_json = json.loads(stickers_config)
    update_stickers_set(stikers, extract_stickers_set(stickers_config_json, 'JUST_REPLY_STICKERS'))
    update_stickers_set(fuck_you_stickers, extract_stickers_set(stickers_config_json, 'FUCK_YOU_STICKERS'))


def select_random(*args):
    """Returns randomly selected argument"""
    return args[random.randint(0, len(args) - 1)]


def are_we_mentioned(message):
    """Checks that bot mentioned in specified message"""
    if not hasattr(message, 'json'):
        return False
    json_val = message.json
    if 'entities' not in json_val:
        return False
    entities = json_val['entities']
    if entities:
        for ent in entities:
            if ent['type'] == 'mention' and mentioned_key in json_val['text']:
                return True
    return False


def get_reply_to_message(message):
    """Returns ID of message specified message replies to"""
    if not hasattr(message, 'reply_to_message'):
        return None
    reply_to_message = message.reply_to_message
    if reply_to_message is None or not hasattr(reply_to_message, 'message_id'):
        return None
    return reply_to_message


def is_replied_to_us(message):
    """Checks that message replies to our own message"""
    reply_to_message = get_reply_to_message(message)
    if reply_to_message is None:
        return False
    replied_to = reply_to_message.from_user
    if replied_to is None or not hasattr(replied_to, 'username'):
        return False
    if replied_to.username == bot_details.username:
        return True
    return False


@bot.message_handler(commands=['kek'])
def handle_start_help(message):
    bot.send_message(message.chat.id, select_random(*keks))


@bot.message_handler(commands=['or'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Ору " + select_random(*ornul))


@bot.message_handler(commands=['info'])
def sendInfo(message):
    bot.send_message(message.chat.id,
                     "Жду пул реквесты тут (и звездочки тоже) -> https://github.com/LikiPiki/UwdIliteBot")


@bot.message_handler(commands=['telki'])
def handle_start_help(message):
    if time < 21 or time >= 6:
        try:
            data = urllib.urlopen('http://api.oboobs.ru/noise/1/').read()
            obj = json.loads(data)
            for img in obj:
                bot.send_photo(message.chat.id, 'http://media.oboobs.ru/noise/' + str(img['id']) + '.jpg')
        except Exception:
            bot.send_message(message.chat.id, select_random(*error))
    else:
        bot.send_message(message.chat.id, select_random(*telki_ne_daut))


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    replied_to_us = is_replied_to_us(message)
    mentioned = are_we_mentioned(message)
    if not replied_to_us and not mentioned:
        return # not our business
    if not replied_to_us and mentioned:
        msg_to_reply = get_reply_to_message(message)
        if msg_to_reply is None:
            # someone mentioned us - fuck off
            msg_to_reply_id = message.message_id
        else:
            # if someone mentioned us in reply to someone else - fuck them
            msg_to_reply_id = msg_to_reply.message_id
        bot.send_sticker(message.chat.id, select_random(*fuck_you_stickers), msg_to_reply_id)
        return
    # just random response otherwise
    random_tuple = select_random((bot.send_message, reply),  # send random text reply
                                 (bot.send_sticker, stikers))  # send random sticker from set
    random_tuple[0](message.chat.id, select_random(*random_tuple[1]), message.message_id)


load_stickers_config()
bot.polling()
