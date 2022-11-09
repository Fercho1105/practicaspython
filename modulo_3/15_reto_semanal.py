import matplotlib.pyplot as plt

print("Ingrese el rango de que quira inegrasr los años de rentas")
año1 = int(input("Desde el año: "))
año2 = int(input("Hasta el año: "))


lista_ventas = []
lista_años = []


for i in range(año1,año2+1,1):
    ventas = int(input(f"Ingrese las ventas del año {i}: "))
    lista_ventas.append(ventas)
    lista_años.append(i)

print(lista_ventas)
print(lista_años)

plt.plot(lista_años,lista_ventas)


plt.plot(lista_años, lista_ventas) 
plt.title(f"Ventas del año {año1} al año {año2}")
plt.show()

