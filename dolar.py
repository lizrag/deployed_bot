import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url = requests.get("https://www.dolar-colombia.com/")

soup = BeautifulSoup(url.content, "html.parser")

resultado = soup.find("span", class_= "exchange-rate exchange-rate_up").get_text()


def telegram_bot_dolar(bot_message):

    bot_token = os.getenv("bot_token")
    bot_chatID = os.getenv("bot_chatID")
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    response = requests.get(send_text)

    return response.json()

test = telegram_bot_dolar(f"el precio del dolar hoy es: {resultado}")

print(test)

