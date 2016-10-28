#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals 

import site 
import os.path 
import logging 
import json
site.addsitedir(os.path.join(os.path.dirname(__file__), 'libs')) 

import telegram 
from flask import Flask, request 


app = Flask(__name__) 

#Токен нашего бота 
TOKEN = '#'
URL = 'badmaninnobot2.appspot.com' 

global bot 
bot = telegram.Bot(token=TOKEN) 



state = {}
upper = {}
bottom = {}

#Вот на эту часть кода мы подключим вебхук 
@app.route('/HOOK', methods=['POST']) 
def webhook_handler(): 
    if request.method == "POST": 
        update = telegram.Update.de_json(request.get_json(force=True))
        try:
            chat_id = update.message.chat.id 
            text = update.message.text
            text = text.lower()
            if text == "/start" or text == "/начать":
                try:
                    bot.sendMessage(chat_id=chat_id, text='Введите просто текст или /help для дополнительных настроек')
                except telegram.TelegramError: print "a"
            elif text == "/help" or text == "?" or text == "/помощь" or text == "помощь" or text == "help":
                try: 
                    bot.sendMessage(chat_id=chat_id, text='Введите просто текст и через "|" язык в фомате ru/en')
                    bot.sendMessage(chat_id=chat_id, text='Пример: Harvey| en')
                    bot.sendMessage(chat_id=chat_id, text='Так же можно попробовать /injustice')
                    bot.sendMessage(chat_id=chat_id, text='/detonator детонатор')
                except telegram.TelegramError: print "a"

            elif text == "/injustice" or text == "/несправедливость":
                image_url = make_mem_custom("Несправедливость!","")
                try:
                    bot.sendPhoto(chat_id=chat_id, photo=image_url.encode("utf-8"))
                except telegram.TelegramError: print "a"
            elif text.startswith("/detonator") or text.startswith("/детонатор"):
                e = text[11:]
                image_url = make_mem_custom("Где " + e + "?" ,"Ты бы не отдал его случайному человеку из толпы.")
                try:
                    bot.sendPhoto(chat_id=chat_id, photo=image_url.encode("utf-8"))
                except telegram.TelegramError: print "a"
            else:
                mess = text.split('|')
                if len(mess)>1:
                    if mess[1].strip()=="ru" or mess[1].strip()=="en":
                        image_url = make_mem(mess[0].strip(), mess[1].strip())
                    else:
                        image_url = make_mem_custom(mess[0].strip(), mess[1].strip())
                else:
                    image_url = make_mem(mess[0].strip())
                try: bot.sendPhoto(chat_id=chat_id, photo=image_url.encode("utf-8"))
                except telegram.TelegramError: print "a"
             
            logging.getLogger().setLevel(logging.INFO) 
            logging.info('===============TEXT=================' + text) 
        except AttributeError:
            print "a"
    return 'ok' 

#А вот так подключается вебхук 
@app.route('/set_webhook', methods=['GET', 'POST']) 
def set_webhook(): 
    s = bot.setWebhook('https://%s/HOOK' % URL) 
    if s: 
        return "webhook setup ok" 
    else: 
        return "webhook setup failed" 

@app.route('/') 
def index(): 
    return '.' 


def make_mem(a, l="ru"):
    mem_id = "82468060"
    url = "https://api.imgflip.com/caption_image"
    import urllib, urllib2
    text0 = a.upper() + ","
    loc=l
    if loc=="ru":
        text1="МОЖЕМ ЛИ МЫ ДОВЕРЯТЬ ЕМУ?"
    else:
        text1= "CAN WE TRUST HIM?"
    post_fields = {'User-Agent' : "Magic Browser",'template_id': mem_id, 'username': 'batman_bot', 'password':'batmanmojemlimidoveryat', 'text0': text0, 'text1': text1}     # Set POST fields here
    post_encoded = {}
    for k, v in post_fields.iteritems():
        post_encoded[k] = unicode(v).encode('utf-8')
    request = urllib2.Request(url, urllib.urlencode(post_encoded).encode(), headers={'User-Agent' : "Magic Browser"})
    j = urllib2.urlopen(request).read().decode()
    ret = json.loads(j)
    logging.info('===============TEXT=================' + j) 
    return ret["data"]["url"]

def make_mem_custom(a, b):
    mem_id = "82468060"
    url = "https://api.imgflip.com/caption_image"
    import urllib, urllib2
    text0 = a.upper() + ""
    text1 = b.upper() + ""
    post_fields = {'User-Agent' : "Magic Browser",'template_id': mem_id, 'username': 'batman_bot', 'password':'batmanmojemlimidoveryat', 'text0': text0, 'text1': text1}     # Set POST fields here
    post_encoded = {}
    for k, v in post_fields.iteritems():
        post_encoded[k] = unicode(v).encode('utf-8')
    request = urllib2.Request(url, urllib.urlencode(post_encoded).encode(), headers={'User-Agent' : "Magic Browser"})
    j = urllib2.urlopen(request).read().decode()
    ret = json.loads(j)
    logging.info('===============TEXT=================' + j) 
    return ret["data"]["url"]



