import telebot
import time
import datetime
import random

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1001816634805'

def formatar_matriz(matriz):
    return "\n".join(f"{i + 1} " + "".join(f"{col}" if col != "🛢" else "🛢" for col in linha) for i, linha in enumerate(matriz))


def gerar_possibilidades_minas():
    possibilidades_minas = []
    for _ in range(1):
        # Inicializa a matriz com "🛢" para representar células vazias
        matriz_mina = [["🛢"] * 3 for _ in range(1)]

        # Escolhe aleatoriamente uma coluna para o diamante (💎) na linha 1
        coluna_diamante_1 = random.randint(0, 2)
        matriz_mina[0][coluna_diamante_1] = "💎"

        possibilidades_minas.append(matriz_mina)

    return possibilidades_minas


texto4 = """
⚠️ <b>Fique atento ao jogo</b> ⚠️

💎 Mr Thimble
🔎 identificando entrada

<a href="https://go.aff.br4-partners.com/iu9afmas?utm_source=Thimbres">📲 <b>Link de cadastro</b></a>
"""

texto5 = """
🔷🔹 <b>Entrada Finalizada</b> 🔹🔷
     ✅✅ <b>GRENN!</b> ✅✅
"""

mensagem = """
💰 Entrada confirmada 💰
⏰ Válido até: {}
🔁 N° de tentativas: 2
👇🏻 <b>Próximas previsões</b> 👇🏻

{}

<a href="https://t.me/c/1816634805/13">Use o slowmotion para ter certeza da entrada</a>

🔗 Link de acesso: <a href="https://go.aff.br4-partners.com/iu9afmas?utm_source=Thimbres"><b>Mr Thimble</b></a>

Reage aqui quem lucrou mais de R$ 15👇

"""

print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)

possibilidades_minas = gerar_possibilidades_minas()

for i, matriz_mina in enumerate(possibilidades_minas, start=1):
    mensagem_formatada = formatar_matriz(matriz_mina)
    validade = datetime.datetime.now() + datetime.timedelta(minutes=2)
    hora_validade = validade.strftime("%H:%M")
    mensagem_formatada = mensagem.format(hora_validade, mensagem_formatada)
    bot.send_message(chat_id=group_id, text=mensagem_formatada, parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(120) 

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(720)
