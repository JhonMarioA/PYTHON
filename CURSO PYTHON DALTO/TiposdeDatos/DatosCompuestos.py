# --------------------------
# Listas: 

listaModificar = ["Mario", 1.85, "Gosling", True] #Listas Modificables

print(listaModificar)
print(listaModificar[0])


listaNoModificar = ("Mario", 1.85, "Gosling", True) #Tupla No Modificables
                    
print(listaNoModificar)
print(listaNoModificar[0])

# listaNoModificar[2] = "A" -> Nos dara un error ya que tuplas no se pueden modicar los elementos de la lista.
 


# --------------------------
# Creando un conjunto (set): 

conjunto = {"Tilin", 123, True} # Podemos redefinir por completo, pero no redefinir elementos individualmente. No se puede acceder por indice (son datos desordenados). No permite repetir elem.
conjunto = {"Ferkd"}


# --------------------------
# Creando un diccionario (dict): 

diccionario = {

'nombre' : "Mario",
'edad' : "18",
'verdadero' : True

}

print(diccionario['edad'])
