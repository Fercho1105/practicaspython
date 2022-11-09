#Guardar e imprimir cosas de una api, usando json 

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"


try:
    respuesta = requests.get(url, timeout=10)
except requests.Timeout:
    print("Error: El tiempo de espera ha finalizado")


if respuesta.status_code != 200:
    print("Pokemon no encontrado")
else:
    print(respuesta)

#############################################################

# datos = respuesta.json()
# nombre = datos["species"]["name"]
# print(nombre)

###############################################################

datos = respuesta.json()
nombre = datos["name"]

print("Movimientos de " + nombre + ":\n")

movimientos = datos["moves"]
for i in range(int(len(movimientos))):
    movimiento = movimientos[i]["move"]["name"]
    print(movimiento)

