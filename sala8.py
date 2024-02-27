import telebot
import time
import datetime
import random

CHAVE_API = "7122848020:AAFLRnw_i11ywvhyAztioEpjfKpAMKGoAms"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002130965866'

texto1 = """
ATENÇÃO!
"""

# Gerar valores aleatórios para a entrada normal e turbo
entrada_normal = random.randint(3, 11)

texto2 = f"""
ENTRADA CONFIRMADA!
Minutos Pagantes: {entrada_normal} min.(Fazer entradas dentro do prazo de minutos)
Validade: -

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
