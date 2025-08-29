"""
Nivel 1: Conceptos Básicos
Operaciones Aritméticas:

 Crea un programa que pida dos números al usuario y muestre su suma, resta, multiplicación, división y módulo.

Comparación de Números:

 Escribe un programa que compare dos números ingresados por el usuario e indique cuál es mayor, menor o si son iguales.

Manejo de Cadenas:

 Solicita al usuario su nombre y apellido en minúsculas y muéstralos en mayúsculas y con la primera letra en mayúscula.


"""

print("___________________________________________________\n")
nro1 = int(input("Ingrese el primer número: "))
nro2 = int(input("Ingrese el segundo número: "))

print(f"La suma de los números es: {nro1 + nro2}")
print(f"La resta de los números es {nro1 - nro2}")
print(f"La multiplicación de los números es {nro1 * nro2}")
print(f"La divisón de los números es {nro1 / nro2}")

print("___________________________________________________\n")

if nro1 > nro2:
    print(f"El número {nro1} es mayor a el número {nro2}")

elif nro2 > nro1:
    print(f"El número {nro2} es mayor a el número {nro1}")

else:
    print("Los números son iguales.")

print("___________________________________________________\n")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(nombre.upper())
print(nombre.capitalize())
print(nombre.title())
print(apellido.capitalize())
