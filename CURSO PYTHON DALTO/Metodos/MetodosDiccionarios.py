
diccionario = {

  "nombre" : "Tesillo",
  "edad"   :  18,
  "Apellido" : "Rio"

}

diccionario.keys()       # Permite iterar sobre las llaves
diccionario["nombre"]     # Si no se encuentra lanza una excepción.
diccionario.get("color") # Si no se encuentra simplemente muestra NONE.
claves = diccionario.keys()
print(claves)

diccionario.pop("nombre") # Permite eliminar un elemento de la lista.
print(diccionario)
 
diccionario_iterable = diccionario.items() # Permite iterar los elementos.
print(diccionario_iterable) 

diccionario.clear()     # Eliminar todo los elementos del diccionario (si se desea sacar varios, se pone ',' y el elemento). 
print(diccionario)

