
frase = input("Ingrese una frase: ")

print(frase)

# Mi versión

numero_palabras = frase.count(" ") + 1
tiempo_empleado = numero_palabras / 2

print(f"El número de palabras es {numero_palabras}.")
print(f"El tiempo empleado en decir la frase es {tiempo_empleado} segundos.")

if tiempo_empleado > 60:
 print("Para flaco tampoco te pedí la biblia.")

tiempo_dalto = tiempo_empleado / 2 * 1.3
print(f"Dalto se demoraría un {tiempo_dalto} segundos. ")


# Versión de dalto.

numeroEs = frase.split(" ")
cantidadP = len(numeroEs)

print("__________________________________________________________________\n")
print(f"El número de palabras es {cantidadP}.")
print(f"El tiempo empleado en decir la frase es {cantidadP / 2} segundos.")

print(f'Dalto la diria en {cantidadP/2 - (cantidadP*100 // 2*0.3 / 100)} segundos.')