import telebot
import datetime
import random
import time

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8" 
bot = telebot.TeleBot(CHAVE_API)
channel_id = '-1002023766660'

possibilidades_minas = [
    "Apostar na 1° e 2° coluna",
    "Apostar na 1° e 3° coluna",
    "Apostar na 2° e 3° coluna",
    "Apostar na 1° e 2° dúzia",
    "Apostar na 1° e 3° dúzia",
    "Apostar na 2° e 3° dúzia",
]

texto4 = """
👀JÁ ESTOU ANALISANDO AS ENTRADAS FAMÍLIA

Às 13:30 começaremos a nossa sessão de operações em DÚZIAS E COLUNAS 🔥🚀

🚨Se você ainda não sabe como pegar as minhas entradas, CLIQUE ABAIXO para assistir as Vídeo-Aulas!👇

👉COMECE POR AQUI <a href="https://t.me/metodofortuna/50"><b>(CLIQUE)</b></a>
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
    time.sleep(1200) 
    bot.send_message(chat_id=channel_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(30)
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
        "09:10"
    ]

    if current_time in signal_times:
        send_signal()

try:
    check_and_send_signal()
except Exception as e:
    print(f"Error occurred: {str(e)}")
