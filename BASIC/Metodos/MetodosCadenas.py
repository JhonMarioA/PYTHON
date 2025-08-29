# METODOS: DATO.METODO()


cadena1 = "Jhon Duran"
cadena2 = "Bomboclan"
cadena3 = "El,día,esta,lluvioso"

(dir(cadena1)) # nos muestra todo lo que podemos hacer con el tipo de dato (En este caso una cadena). (Función)
cadena1.upper() # pasar todo a mayus (podemos poner el upper despues de una cadena directamente " "...)
cadena1.lower() # pasar todo a minus
cadena1.capitalize() # capitalizar texto
cadena1.find("D") # comparar cadenas, devuelve la posición de lo que buscamos (Si no hay coincidencias devuelve -1).
cadena1.index("J") # comparar cadenas, (Si no hay coincidencias devuelve una excepción)
cadena1.isnumeric() # verifica si son números
cadena1.isalpha() # verifica si son letras (a-z, sin contar los espacios)
cadena1.count("n") # cuenta caracteres en la cadena
len(cadena1) # función "Len" cuenta los caracteres de una cadena.
cadena1.startswith("Jh") # verificar si una cadena empieza por...
cadena1.endswith("ran") # verificar si una cadena termina por...
cadena3.replace(",", " ") # remplazar una sección de la cadena.
cadena3.split(",") # separa la cadena, en más cadenas si encuentra el parametro ingresado (lo devuelve en lista).


resultado = cadena3.replace(",", " ")

print(resultado)