import telebot
import datetime
import random
import time

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 
bot = telebot.TeleBot(CHAVE_API)
channel_id = '-1002235131292'

possibilidades_minas = [
"🟦",
"🟥",
]

texto4 = """
⚠ Fique atento ao jogo ⚠

⚽ FOOTBALL STUDIO

🔎 identificando entrada

<a href="https://baraodabet.com/main?openedModals=%2Fsign-up"><b>🖥 Link de cadastro</b></a>
"""

texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
"""

mensagem = """
✅ Entrada Confirmada 

👉 Entrada:{}

⚠ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  

⏱ Válido até: {}


<a href="https://baraodabet.com/main?openedModals=%2Fsign-up"><b>📲 Plataforma correta</b></a>
"""

bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60) 
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
validade = datetime.datetime.now() + datetime.timedelta(minutes=10)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)
bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(30)
bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(210)

