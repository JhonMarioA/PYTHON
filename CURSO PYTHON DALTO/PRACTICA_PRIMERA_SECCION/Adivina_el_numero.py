# Juego de adivina el número
import random

dif = input("Por favor ingrese la dificultad (F, M, D): ")

if(dif == "F"):
    MAX = 10
elif (dif == "M"):
    MAX = 50
elif (dif == "D"):
    MAX = 100
else:
    print("Dificultadad no valida")
    MAX = 10

MIN = 1

numeroC = random.randint(MIN, MAX)
intentos = 0;
while True:


    numero = int(input("Por favor ingrese el numero: "))
    intentos += 1; 
    if(numero == numeroC):
        print(f"El número es correcto, lo hizo en {intentos} intentos.")

        break
    elif(numeroC > numero):
        print("El número a adivinar es mayor.")

    elif(numeroC < numero):
        print("El número a adivinar es menor.")
    
    else:
        print("El número no es correcto, intentelo de nuevo.")
    
