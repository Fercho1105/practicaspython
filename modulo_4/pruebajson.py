import json

nombre = input("Ingrese un nombre: ")
edad = input("Ingrese su edad: ")

json_persona = {"nombre" : nombre, "edad" : edad}

with open("C:/Users/elchi/Documents/pru_json/prueba_json.json", "a") as json1 :
    json.dump(json_persona,json1)

# full_name = input("What is your name? ")
# email = input("Whats your email address ")
# school_id =(input("Enter your school ID "))
# filename = 'sing_user.json'

# with open(filename, 'w') as f_obj:
#     #diccionario que contiene todo
#     user = {
#         "full name" : full_name,
#         "Email address" : email,
#         "School Id": school_id
#         }

#     json.dump(user,f_obj, indent=4)