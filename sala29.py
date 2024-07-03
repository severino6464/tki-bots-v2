import telebot
import datetime
import random
import time

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 
bot = telebot.TeleBot(CHAVE_API)
channel_id = '-1002023766660'

possibilidades_minas = [f"Apostar no número {i} (com oito vizinhos na pista)" for i in range(1, 37)]
possibilidades_minas.append("Apostar no número 0 (com oito vizinhos na pista)")

texto4 = """
🤑Falaaa tropa, em 15 minutos já começa nossa sessão EM NÚMEROS! Se preparem e vamos pra cima!🚀

 👉CLIQUE AQUI (Passo-a-passo) (https://t.me/metodofortuna/50)

‼️Ainda tem dúvidas, ou não sabe como operar comigo? <a href="https://t.me/metodofortuna/50"><b>👉COMECE POR AQUI(CLIQUE)</b></a>
"""

texto5 = """
ABRAM A AUTO MEGA, VAMOS INICIAR!🔥💸

<a href="https://bantubet.co.ao/affiliates/?btag=1786461"><b>👉CLIQUE AQUI PARA ABRIR A CORRETORA</b></a>
"""

texto6 = """
✅ SESSÃO FINALIZADA ✅
"""

mensagem = """
🎯 Entrada Confirmada 🎯

🖥 Roleta: Auto Mega Roulette
🔥 Entrada: {}
🛟 Até dois Gales - Cubra o zero!

🧨 Último número: {}


<a href="https://t.me/metodofortuna/50"><b>🍀Clique aqui se ainda tem dúvidas!</b></a>
"""

def send_signal():
    bot.send_message(chat_id=channel_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(900) 
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    n_jogadas = random.randint(1, 37)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, n_jogadas)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    n_jogadas = random.randint(1, 37)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, n_jogadas)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)
    
    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    n_jogadas = random.randint(1, 37)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, n_jogadas)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    n_jogadas = random.randint(1, 37)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, n_jogadas)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(300)

    possibilidade_mina_aleatoria = random.choice(possibilidades_minas)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    n_jogadas = random.randint(1, 37)
    mensagem_formatada = mensagem.format(possibilidade_mina_aleatoria, n_jogadas)
    bot.send_message(chat_id=channel_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(30)
    bot.send_message(chat_id=channel_id, text=texto6, parse_mode='HTML', disable_web_page_preview=True)

    

def check_and_send_signal():
    current_time = datetime.datetime.now().strftime("%H:%M")
    signal_times = [
        "14:45"
    ]

    if current_time in signal_times:
        send_signal()

try:
    check_and_send_signal()
except Exception as e:
    print(f"Error occurred: {str(e)}")
