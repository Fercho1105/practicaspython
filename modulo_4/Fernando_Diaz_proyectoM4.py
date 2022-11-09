#Importamos las librerias a usar
import requests  #Para hacer peticiones "get"
#Para mostrar imagenes al usuario y obtener el link de la imagen de un pokemon 
import matplotlib.pyplot as plt   
from PIL import Image  
from urllib.request import urlopen 
import json  #Para usar,crear,editar archivos json



#Obtenemos al Pokemon
pokemon = input("Ingrese un pokemon: ") ##Le pedimos al usuario que nos indique de qué pokemon quiere obtener los datos


#Obtenemos respuesta
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"  #Agregamos el pokemon al url de la peticion
respuesta = requests.get(url)  #Obtenemos la respuesta 

#Tiempo de respuesta
try:
    respuesta = requests.get(url, timeout=10)   #Nos aseguramos que haya un tiempo de espera/respuesta menor a 10 segundos
except requests.Timeout:
    print("Error: El tiempo de espera ha finalizado") #Sino se arrojara un mensaje de error 


#Que sea peticion valida
if respuesta.status_code != 200 :
    print("Pokemon no encontrado")  #Nos aseguramos que sea una respuesta valida y que el pokemon exista, y de no ser así, se acabará el programa
    exit()
else:
    print("Todo bien")  #Si es una peticion exitosa, proseguiremos con el programa


#Hacemos un archivo jason con los datos del pokemon ingresado
datos = respuesta.json()




##Nombre
nombre = datos["name"]  #Obtenemos el nombre del pokemon
# print(f"Nombre: {nombre}")


###MOVIMIENTOS
print("Movimientos de " + nombre + ":")
movimientos = datos["moves"]  #Obtenemos sus movimientos del pokemon y los almacenamos en una lista
movs = []
for i in range(int(len(movimientos))):
    movimiento = movimientos[i]["move"]["name"]
    # print(movimiento)
    movs.append(movimiento)



##TAMAÑO       
tamaño = datos["height"] #Obtenemos el tamaño del pokemon
# print(f"Tamaño: {tamaño}")

#PESO
peso = datos["weight"] #Obtenemos el peso del pokemon
# print(f"Peso: {peso}")


#TIPOS
tipo = datos["types"][0]["type"]["name"] #Obtenemos el tipo del pokemon
# print(f"Tipo: {tipo}")


#Imagen
try:
    url_imagen = datos["sprites"]["front_default"] #Ya que algunos pokemones no tienen imagenes, arrojamos un mensaje si es que no se encuentra una imagen
    imagen = Image.open(urlopen(url_imagen))
except:
    print("El pokemon no tiene imagen")
    exit()


#Mostramos imagen
plt.title(datos["name"])
imgplot = plt.imshow(imagen)
plt.show()


#Empezamos a darle el formato del archivo
#Hacemos un diccoinario con los datos obtenidos, ya que los archivos json tienen ese formato
json_poke = {'Nombre' : f'{nombre}', 'Peso ' : f'{peso}', 'Movimientos ': f'{movs}', 'Tamaño ' : f'{tamaño}', 'Tipo ' : f'{tipo}', 'Url de imagen ' : f'{url_imagen}'}
print(json_poke) #Imprimimos los datos del pokemon


#Convertimos los datos a archivo json y guardamos el archivo en cierta carpeta con el respectivo nombre
with open(f"C:/Users/elchi/Documents/Curso Python Ucamp/pokedex/{nombre}.json", "w") as json1 :  #En este caso, así era mi ruta para guardar los archivos la carpeta pokedex
    json.dump(json_poke,json1)

