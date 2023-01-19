import requests
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

load_dotenv()

def get_dolar_value():
    url = 'https://www.dolar-colombia.com/'
    page = requests.get(url)
    dolar_value = page.json()["dolar"]["venta"]
    return dolar_value

def handle_commands(bot, update):
    if update.message.text == '/dolar':
        dolar_value = get_dolar_value()
        bot.send_message(chat_id=update.message.chat_id, text='Valor del dólar en Colombia: ' + dolar_value)

updater = Updater(token='TELEGRAM_TOKEN_DOLAR')
updater.dispatcher.add_handler(CommandHandler('dolar', handle_commands))
updater.start_polling()
updater.idle()
