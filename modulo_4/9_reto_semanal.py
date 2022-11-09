import requests

while True:

    print("""
    Bienvenido a la API weather.
    "¿Cómo desea obtener su clima.
    1) Por coordenadas
    2) Por nombre de la ciudad
    3) Salir
    """)
    opcion = input("Ingrese una opcion: ")


    if opcion == "1":
        while True:
            try:
                latitud = input("Ingrese la latitud de sus coordenadas: ")
                float(latitud)

                longitud = input("Ingrese la longitud de sus coordenadas: ")
                float(longitud)
                break

            except ValueError:
                print("Valores incorrectos, vuelva a introducir los valores nuevamente.")


        while True:
            api_key = input("Ingrese su API key: ")
            if api_key == "":
                print("Ingrese su API Key, no puede dejar valores vacios.")
            else:
                break

        url_destino = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}&lang=es"

        respuesta = requests.get(url_destino)

        if respuesta.status_code != 200:
            print("Ha ocurrido un error. Intenta Nuevamente")
            exit()

        datos = respuesta.json()
        ciudad = datos["name"]

        datos_clima = datos["weather"]
        clima = datos_clima[0]["description"]

        print(f"El clima de la ciudad {ciudad} es {clima}")
        break





    elif opcion == "2":

        while True:
            lugar = input("Ingrese el nombre del lugar del que quiere obtener el clima: ")
            
            if lugar.isalpha():
                lugar.capitalize()
                break
            else:
                print("Nombre invalido, intente nuevamente.")

        while True:
            api_key = input("Ingrese su API key: ")
            if api_key == "":
                print("Ingrese su API Key, no puede dejar valores vacios.")
            else:
                break


        url_destino = f"https://api.openweathermap.org/data/2.5/weather?q={lugar}&appid={api_key}&lang=es"

        respuesta = requests.get(url_destino)



        if respuesta.status_code == 401:
            print("API Incorrecta")
            print("Intente NUevamente")
            exit()


        elif respuesta.status_code == 404:
            print("Ciudad No Encontrada")
            print("Intente NUevamente")
            exit()

        elif respuesta.status_code != 200:
            print("Ha ocurrido un error. No se ha encontrado la ciudad Intenta Nuevamente")
            print("Intente NUevamente")
            exit()




        datos = respuesta.json()
        ciudad = datos["name"]

        datos_clima = datos["weather"]
        clima = datos_clima[0]["description"]

        print(f"El clima de la ciudad {ciudad} es {clima}")
        break





    elif opcion == "3":
        exit()

    else:
        print("Valor desconocido, inserte una opcion valida")
    





