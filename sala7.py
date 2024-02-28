import telebot
import time
import datetime
import random

CHAVE_API = "6722903231:AAE_Z5PhwNMjmo0rDXxkz8oeQJNP9Uc8qWg"

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002146987560'

texto1 = """
ATENÇÃO!
"""
  
texto2 = f"""
ENTRADA CONFIRMADA!
Entrar: {entrada_normal}x teste e {entrada_turbo}x turbo
Validade: 3 minutos

"""

texto3 = """
ENTRADA ENCERRADA
"""

bot.send_message(chat_id=group_id, text=texto1, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(10)
bot.send_message(chat_id=group_id, text=texto2, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(100)
bot.send_message(chat_id=group_id, text=texto3, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(10)
