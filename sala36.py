import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

# Defina sua chave API
CHAVE_API = "6845510395:AAEIUgZ8ecAGxHom_scL0-6ijSaY4ZfkMCg"
bot = telebot.TeleBot(CHAVE_API)

# Mensagens a serem enviadas
texto2 = """
Parabéns pela sua decisão porque me chamou a tempo de garantir uma vaga no nosso grupo de Prêmios gratuitos 🎁
"""

texto3 = """
Eu vou te entregar vários prêmios, faço isso para ajudar os meus seguidores...

O primeiro passo para realizar os seus sonhos comigo é clicando no botão abaixo 👇🏽
"""

# Função que lida com o comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name

    texto1 = f"Opaa, {first_name}, tudo bem?"

    try:
        bot.send_message(chat_id=chat_id, text=texto1, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(3)
        bot.send_message(chat_id=chat_id, text=texto2, parse_mode='HTML', disable_web_page_preview=True)
        time.sleep(2)

        # Cria um botão com um link
        keyboard = InlineKeyboardMarkup()
        button = InlineKeyboardButton(text="Acessar Grupo", url="https://t.me/Vipdajujuferrari")
        keyboard.add(button)

        bot.send_message(chat_id=chat_id, text=texto3, reply_markup=keyboard, parse_mode='HTML', disable_web_page_preview=True)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Inicia o bot
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"Erro no polling: {e}")
        time.sleep(15)
