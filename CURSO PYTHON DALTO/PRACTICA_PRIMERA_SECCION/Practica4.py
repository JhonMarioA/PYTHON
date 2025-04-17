
"""Nivel 2: Condicionales y Bucles
Edad y Acceso:

Pregunta la edad al usuario y muestra si es menor de edad, adulto o adulto mayor.

Verificación de Contraseña:

Crea un programa que almacene una contraseña y pida al usuario que la ingrese hasta que acierte.

Número Par o Impar:

Pide un número y muestra si es par o impar."""


print("___________________________________________________\n")

edad = int(input("Ingrese su edad: "))

if edad >= 80:
    print("\nUsted es adulto mayor de edad.")

elif edad >= 18:
    print("\nUsted es mayor de edad")

else: print("\nUsted es menor de edad.")


print("___________________________________________________\n")

contra = "Bomboclan"

encontrado = False
while encontrado == False:

   contraU = input("Ingrese su contraseña: ")

   if contraU.find(contra) != -1:
    print("\nContraseña correcta.")
    encontrado = True

numero3 = int(input("\nIngrese un número: "))

if numero3 % 2 == 0:
   print("El número es par.")

else: print("El número es impar.")



import os
import time

time.sleep(3)
os.system('cls')