import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001850447368'

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

texto1 = """
🎲 Fique atento ao jogo 🎲
💣 Mines - Entrada em 2 minutos
🔎 Estamos validando uma entrada
<a href="https://go.aff.br4-partners.com/gdp9s2xv">🖥 Link de cadastro</a>
"""

mensagem = """
🎲 Entrada confirmada 🎲
🥇: Entrada 

{}
🎮: Tentativas: 2
Jogar com 2 a 3 minas

⏱️ Válido até: {}

<a href="https://go.aff.br4-partners.com/gdp9s2xv">📲: Plataforma correta</a>
<a href="https://go.aff.br4-partners.com/gdp9s2xv">👉🏻: Link do jogo</a>

Quem lucrou acima de R$ 10 reage aqui embaixo 👇
"""


text2 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 Você que fez GREEN envie um print no @suportereidomines
  """


print("=====")
bot.send_message(chat_id=group_id, text=texto1, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120)
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
link_aleatorio = random.choice(links)
validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
mensagem_formatada = mensagem_formatada.replace("LINK_PLATAFORMA_CORRETA", link_aleatorio)
mensagem_formatada = mensagem_formatada.replace("LINK_JOGO", link_aleatorio)
bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(30)
time.sleep(90)
bot.send_message(chat_id=group_id, text=text2 ,parse_mode='HTML', disable_web_page_preview=True)
time.sleep(180)  # Espera 5 minutos (300 segundos)
