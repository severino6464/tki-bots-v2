import time
import requests
import telebot

ultimos_resultados = []
check_resultados = []
ultima_aposta = None  # Variável para rastrear a última aposta

token = '5597794728:AAGfwOg3RijfPrQ5S_Iw6NKAuYucNEdIsO8' #fox bot
chat_id = '-1001808094144'


texto4 = """
⚠️ ANALISANDO ENTRADAS⚠️

🎰 Roleta: Brasileira 

🖥 Link de cadastro:[Clique aqui](https://bsbet.online?c=bonus)
"""



# Função para puxar os dados da roleta
def puxar_dados():
    global ultimos_resultados
    # Faz uma requisição GET para a URL específica
    resposta = requests.get(url, headers=headers)
    dic_resposta = resposta.json()
    dados = dic_resposta['gameTables']
    for i in dados:
        roletas = i['gameTableId']
        # Puxando os últimos resultados apenas da roleta brasileira
        if '103910' in roletas:
            chaves = i.keys()
            if 'lastNumbers' in chaves:
                ultimos_resultados = i['lastNumbers']
    return ultimos_resultados

# Função para determinar a cor do número (vermelho ou preto)
def determinar_cor(numero):
    vermelhos = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
    if numero in vermelhos:
        return "VERMELHO"
    else:
        return "PRETO"

# Função para enviar mensagem para o Telegram
def enviar_mensagem_telegram(mensagem):
  
    bot = telebot.TeleBot(token=token)
    bot.send_message(chat_id=chat_id, text=mensagem,parse_mode='Markdown')

url = "https://casino.betfair.com/api/tables-details"
headers = {"cookie": "vid=8ab7daa7-57f7-4196-8285-943390594163"}


ultimos_resultados.clear()
puxar_dados()

if ultimos_resultados != check_resultados:
    check_resultados = ultimos_resultados
    primeiro_numero = ultimos_resultados[0]
    segundo_numero = ultimos_resultados[1]
    terceiro_numero = ultimos_resultados[2]
    quarto_numero = ultimos_resultados[3]
    x1 = determinar_cor(primeiro_numero)
    x2 = determinar_cor(segundo_numero)
    x3 = determinar_cor(terceiro_numero)
    x4 = determinar_cor(quarto_numero)

    if x1 == x2 == x3:
        cor_aposta = "🔴" if x1 == "PRETO" else "⚫"
        ultima_aposta = x1
        mensagem = f"""
        💰 PADRÃO INDETIFICADO 💰
        🚀 Entrada Confirmada
        🎰 Roleta: Brasileira 

        Entrar na cor: {cor_aposta}

        🟢 Sempre Cobrir o Zero
        🚨 Aplicar até 2 gales
    
        🎯[APOSTE AQUI](https://bsbet.online?c=bonus)
        🎁 [Clique aqui](https://bsbet.online?c=bonus)
"""
        enviar_mensagem_telegram(mensagem)
        print(mensagem)
        time.sleep(45)
           
            
    else:
        mensagem = f"O primeiro número foi: {primeiro_numero}, e ele é da cor: {x1}\n"
        mensagem += f"O segundo número foi: {segundo_numero}, e ele é da cor: {x2}\n"
        mensagem += f"O terceiro número foi: {terceiro_numero}, e ele é da cor: {x3}"

       
    print(mensagem)

if ultima_aposta is not None:
        puxar_dados()
        novo_resultado = determinar_cor(ultimos_resultados[0])
        if novo_resultado == ultima_aposta:
            mensagem_aposta_vencedora = f" RED ❌"
            enviar_mensagem_telegram(mensagem_aposta_vencedora)
            ultima_aposta = None  # Limpa a última aposta
            time.sleep(10)
             
            bot = telebot.TeleBot(token=token)
            bot.send_message(chat_id=chat_id, text=texto4, parse_mode='Markdown')

           
        else:
            mensagem_aposta_perdedora = f" GREENN ✅✅"
            enviar_mensagem_telegram(mensagem_aposta_perdedora)
            ultima_aposta = None  # Limpa a última aposta
            time.sleep(10)
              
            bot = telebot.TeleBot(token=token)
            bot.send_message(chat_id=chat_id, text=texto4, parse_mode='Markdown')

   
time.sleep(5)
