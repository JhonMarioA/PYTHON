


animales = {"Perro", "Gato", "Vaca", "Delfin"}
numeros = {14,34,56,24}

for animal in animales:
    print(f"El animal es {animal}")

print("\n\n")

for numero in numeros:
    print(f"El numero {numero} * 2 es: {numero*2}")

print("\n\n")


for animal,numero in zip(animales, numeros):  # Podemos iterar dos conjuntos a la vez (O más), solo si tienen la misma cantidad de elementos.
    print(f"El animal es {animal}")
    print(f"El numero {numero} * 2 es: {numero*2}")

print("\n")

for num in range(5, 10): # En un rango especifico.
    print(f"num: {num}")

print("\n")

for num in range(5): # De 0 al n-1 indicado.
    print(f"num: {num}")


print("\n")

for num in enumerate(numeros):  # Forma optima de recorrer una conjunto por su indice.
    indice = num[0]
    valor = num[1]
    print(f'El indice es {indice} y el valor es {valor}')

print("\n")

for num in numeros: # Usando el else, se ejecuta despues de terminar de recorrer la conjunto.
    print(num)
else:
    print("El bucle termino")


# Todo lo anterior funciona exactamente igual para tuplas 



