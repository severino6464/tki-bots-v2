import telebot
import time
import datetime

CHAVE_API = "5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8"  # BOT FOX

bot = telebot.TeleBot(CHAVE_API)

group_id = '-1002037866876'

texto4 = """
⚠️ <b>OPORTUNIDADES IDENTIFICADAS!</b> ⚠️
"""

texto5 = """
     <b>Entradas Finalizadas!!!!</b>
✅✅ <b>LUCROOO!</b> ✅✅
"""

# Estrutura de dados para os animais
animais = [
    {
        'nome': 'Tiger',
        'mensagem': """
🚨 <b>HORÁRIOS QUE TÃO PAGANDO MUITO, APROVEITEM!</b> 🚨

💰 Entradas confirmadas! 💰
🐯 Fortune Tiger 🐯

(99,72% de Assertividade) ✅

🕑 <b>Apostem nesses horários abaixo</b>:

🐯{} 
🐯{} 
🐯{} 
🐯{} 
🐯{} 
🐯{} 
🐯{}

<a href="https://bit.ly/vex-bet">🎰 <b>CADASTRE-SE PARA JOGAR</b></a>

<a href="https://bit.ly/vex-bet">Link do jogo!</a>
"""
    },
    {
        'nome': 'Ox',
        'mensagem': """
🚨 <b>HORÁRIOS QUE TÃO PAGANDO MUITO, APROVEITEM!</b> 🚨

💰 Entradas confirmadas! 💰
🐂 Fortune Ox 🐂

(99,72% de Assertividade) ✅

🕑 <b>Apostem nesses horários abaixo</b>:

🐂{} 
🐂{} 
🐂{} 
🐂{} 
🐂{} 
🐂{} 
🐂{}

<a href="https://bit.ly/vex-bet">🎰 <b>CADASTRE-SE PARA JOGAR</b></a>

<a href="https://bit.ly/vex-bet">Link do jogo!</a>
"""
    },
    {
        'nome': 'Mouse',
        'mensagem': """
🚨 <b>HORÁRIOS QUE TÃO PAGANDO MUITO, APROVEITEM!</b> 🚨

💰 Entradas confirmadas! 💰
🐭 Fortune Mouse 🐭

(99,72% de Assertividade) ✅

🕑 <b>Apostem nesses horários abaixo</b>:

🐭{} 
🐭{} 
🐭{} 
🐭{} 
🐭{} 
🐭{} 
🐭{}

<a href="https://bit.ly/vex-bet">🎰 <b>CADASTRE-SE PARA JOGAR</b></a>

<a href="https://bit.ly/vex-bet">Link do jogo!</a>
"""
    }
]

print("=======")
bot.send_message(chat_id=group_id, text=texto4, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(60)

# Itera sobre os animais e envia as mensagens
for animal in animais:
    entrada1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
    hora_validade1 = entrada1.strftime("%H:%M")
    entrada2 = datetime.datetime.now() + datetime.timedelta(minutes=3)
    hora_validade2 = entrada2.strftime("%H:%M")
    entrada3 = datetime.datetime.now() + datetime.timedelta(minutes=5)
    hora_validade3 = entrada3.strftime("%H:%M")
    entrada4 = datetime.datetime.now() + datetime.timedelta(minutes=8)
    hora_validade4 = entrada4.strftime("%H:%M")
    entrada5 = datetime.datetime.now() + datetime.timedelta(minutes=11)
    hora_validade5 = entrada5.strftime("%H:%M")
    entrada6 = datetime.datetime.now() + datetime.timedelta(minutes=14)
    hora_validade6 = entrada6.strftime("%H:%M")
    entrada7 = datetime.datetime.now() + datetime.timedelta(minutes=17)
    hora_validade7 = entrada7.strftime("%H:%M")

    mensagem_formatada = animal['mensagem'].format(
        hora_validade1, hora_validade2, hora_validade3, hora_validade4, hora_validade5, hora_validade6, hora_validade7)

    bot.send_message(chat_id=group_id, text=mensagem_formatada,
                     parse_mode='HTML', disable_web_page_preview=True)
    time.sleep(360)

bot.send_message(chat_id=group_id, text=texto5, parse_mode='HTML', disable_web_page_preview=True)
time.sleep(900)
