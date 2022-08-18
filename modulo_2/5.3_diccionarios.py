# # ****DICCIONARIOS****
""" No hay orden, ni indice, hay identificadores mediante llaves"""

"""EJEMPLO DE UN DICCIONARIO"""

from tkinter import image_names


tiempos = {
    "Hamilton": "1:49.8",
    "Bottas": "1:56.4",
    "Peres": "1:53.8",
    "Verstappen": "1:52.6"  # No hay coma en el ultimo elemento
}


""" FUNCIONES, O METODOS"""

""" .items() """
print(tiempos.items()) # Obtenemos una lista de tuplas a partir del diccionario, de cada llave con su respectuvo valor

""" .keys() """
print(tiempos.keys()) # Obtenemos solo las claves, es decir, solo nos devuelve lo que esta detras de cada dos puntos( : ) en una lista

""" .values() """

print(tiempos.values()) # Obtenemos solo los valores, es decir, solo nos devuelve lo que esta delante de cada dos puntos( : ) en una lista


""" .get() """
print(tiempos.get("Hamilton"))  # Encontramos el valor de una llave 


print(tiempos.get("hamilton", "No encontrado"))  # Si no hay un valor que buscamos, ponemos en otro parametro opcional, lo que sea | sintaxis    diccionario.get(elemento a buscar, parametro si no se encuentra)
