#Obtener acceso a una API con acceso restringido

import requests

latitud = 20.4290299
longitud = -99.3563108

api_key = ""


url_destino = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}"

respuesta = requests.get(url_destino)

if respuesta.status_code != 200:
    print("Ha ocurrido un error. Intenta Nuevamente")
    exit()


datos = respuesta.json()
ciudad = datos["name"]

datos_clima = datos["weather"]
clima = datos_clima[0]["description"]

print(f"El clima de la ciudad {ciudad} es {clima}")
