import os
import requests
import telebot
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()


# Variables de entorno para el token de Telegram y el token de Slack
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
SLACK_TOKEN = os.environ['SLACK_TOKEN']

# Inicializar el bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Inicializar el cliente de Slack
slack_client = WebClient(token=SLACK_TOKEN)

# Función para manejar los mensajes recibidos en Telegram

@bot.message_handler(func=lambda message: True)
def echo_message(message):

    # Obtener el contenido del mensaje
    text = str(message.text)


# Enviar el mensaje a Slack
    url = "https://hooks.slack.com/services/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"
    result = requests.post(url, json={"text": text})
    if(result.text == "ok"):
        print("el mensaje ha sido enviado")
    else:
        print(result.text)


# Iniciar el bot de Telegram
bot.polling()


