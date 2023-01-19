import requests
import json
import os
from flask import Flask
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)



api = requests.get("https://www.el-tiempo.net/api/json/v2/home")
json_data = json.loads(api.content)


def tiempoCiudades(ciudades):

    ciudades = json_data["ciudades"]
    estadoCielo = ""
    temperatura = ""

    for ciudadData in ciudades:
        if ciudadData["nameProvince"] == ciudades:
            estadoCielo = ciudadData["stateSky"]["description"]
            temperatura = ciudadData["temperatures"]
    texto_final = f"Prediccion del Clima hoy en {ciudades}\nCielo {estadoCielo}\n temperatura {temperatura} "
    

    return texto_final

tiempo = tiempoCiudades("Barcelona")



url = "https://hooks.slack.com/services/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"
result = requests.post(url, json={"text": tiempo})
if(result.text == "ok"):
        print("el mensaje ha sido enviado")
else:
        print(result.text)


# slack_event_adapter = SlackEventAdapter(signing_secret,'/slack/events/',app)

# #client = slack.webclient

# if __name__ == "__main__":
#     app.run(debug = True)

# Función para manejar los mensajes recibidos en Telegram

