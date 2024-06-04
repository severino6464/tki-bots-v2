import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002248526405'

possibilidades_minas = [
"‼️ RETIRAR EM 1.50x",
"‼️ RETIRAR EM 2.00x",
"‼️ RETIRAR EM 2.00x",
"‼️ RETIRAR EM 3.50x",
"‼️ RETIRAR EM 1.04x",
"‼️ RETIRAR EM 2.30x",
"‼️ RETIRAR EM 5.00x"
     
 
]



texto4 = """
⚠️ Fique atento ao jogo ⚠️

✈️ Aviator 
🔎 identificando entrada

<a href="https://18k.bet/ac/aviator18k"><b>🖥 Link de cadastro</b></a>
"""


texto5 = """
🔷🔹 Entrada Finalizada 🔹🔷
     ✅✅ GRENN! ✅✅
 
"""



mensagem = """
✅ Entrada Confirmada 

{}

⚠️ MÁXIMO 2 GALES 
🔔 Entrada Confirmada 🔔  
✅ Entrar Agora  

⏱️ Válido até: {}

<a href="https://18k.bet/ac/aviator18k"><b>🖥 Link de cadastro</b></a>
"""





print("=======")

bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(120) 



  
possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
validade = datetime.datetime.now() + datetime.timedelta(minutes=3)
hora_validade = validade.strftime("%H:%M")
mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, hora_validade)

bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)

time.sleep(60)  # Espera 5 minutos (300 segundos)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(180) 
