import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002200526019'

sticker_file_id = 'CAACAgIAAxkBAAMmZSb_ngXS-jrJPaIDkQxNkCtYOQQAAtgLAAJYD5hKNPj69b5xWK8wBA'

possibilidades_minas = [
    "💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",
    "💣💣⭐️💣⭐️\n💣⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️⭐️⭐️\n💣💣⭐️💣💣",
    "💣💣💣⭐️⭐️\n💣💣💣⭐️💣\n💣⭐️⭐️⭐️💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣💣💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣⭐️⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️💣💣💣⭐️\n💣💣⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣💣💣\n⭐️💣⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣",
    "💣⭐️💣⭐️💣\n💣💣💣⭐️💣\n💣💣⭐️⭐️💣\n💣💣⭐️⭐️💣\n💣💣⭐️💣💣",
    "⭐️⭐️⭐️💣💣\n💣⭐️⭐️💣💣\n💣💣💣💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "💣💣💣💣💣\n💣💣💣💣⭐️\n⭐️💣⭐️💣💣\n💣💣⭐️💣💣\n💣💣⭐️💣💣",
    "⭐️⭐️💣💣💣\n💣⭐️💣💣💣\n💣⭐️⭐️⭐️💣\n💣💣💣💣💣\n💣💣💣💣💣",
    "⭐️⭐️💣⭐️💣\n💣💣💣⭐️⭐️\n💣💣💣💣💣\n💣💣💣💣💣\n💣⭐️⭐️⭐️💣",
    "💣💣💣💣⭐️\n⭐️💣💣⭐️💣\n⭐️⭐️⭐️💣💣\n💣⭐️💣💣💣\n💣⭐️💣💣💣",
    "⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣💣💣\n💣⭐️💣⭐️💣",
    "⭐️⭐️⭐️💣💣\n⭐️💣⭐️💣💣\n💣💣💣💣💣\n💣💣💣💣💣\n💣💣💣⭐️💣",
    "⭐️💣💣💣💣\n⭐️💣💣⭐️💣\n💣💣💣💣💣\n💣💣⭐️⭐️💣\n💣💣⭐️⭐️⭐️",
    "💣💣💣💣⭐️\n⭐️💣💣⭐️💣\n⭐️💣⭐️⭐️💣\n💣💣💣💣💣\n💣💣⭐️⭐️💣",
    "💣💣💣⭐️💣\n⭐️💣💣⭐️⭐️\n⭐️💣💣💣💣\n💣💣💣💣💣\n💣💣💣⭐️💣",
    "⭐️💣💣💣💣\n💣💣💣💣💣\n⭐️💣💣💣💣\n💣⭐️💣⭐️💣\n💣⭐️💣⭐️💣"
]

links = [
    "https://exemplo1.com",
   
]



mensagem = """
🎲 Entrada confirmada 🎲
🥇: Entrada 

{}
🎮: Tentativas: 2
Jogar com 2 a 3 minas

⏱️ Válido até: {}

<a href="https://bcraft.g2afse.com/click?pid=1697&offer_id=69">📲: Plataforma correta</a>
"""


text2 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
  """

print("=====")

possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
   
time.sleep(120)
bot.send_sticker(chat_id=group_id, sticker=sticker_file_id)
time.sleep(180)
