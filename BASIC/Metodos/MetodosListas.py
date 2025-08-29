
lista = list(["Tolon", "Bomboclan", 200, True]) # Creando una lista con list()
lista2 = list([45,23,2,False, True, False, 67,10])

len(lista) #Función para contar los elementos de la lista.

resultado = len(lista)
lista.append("Fin") # Agregar al final de la lista.
lista.insert(2, "Pos 2") # Agregar en una posición especifica.
lista.extend([False, 2020]) # Agregar una lista al final.

print(lista)
print(lista2)

lista.pop(0) # Eliminar elemento con su indice.
lista.pop(-1)
lista.remove("Bomboclan") # Eliminar un elemento especifico. 
lista2.sort() # Ordena la lista, de manera asendente.
lista.reverse()
lista.index(200) # Buscar un elemento completo. 
#lista.clear() # Eliminar todos los elementos.

print(lista)
print(lista2)