import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002023633024'

sticker_file_id = 'CAACAgEAAxkBAAMCZSbmh4EopfmSJgx8Z8sDxkeWf1UAAvwAAzgOghFAju2fQymOBzAE'

texto1 = """
ATENÇÃO!
"""

# Gerar valores aleatórios para a entrada normal e turbo
entrada_normal = random.randint(3, 11)
entrada_turbo = random.randint(5, 15)

texto2 = f"""
ENTRADA CONFIRMADA!
Entrar: {entrada_normal}x normal e {entrada_turbo}x turbo
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
