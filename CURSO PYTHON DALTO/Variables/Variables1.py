

num = 10
num += 5
num += 5

print(num)

saludo = "Hola "
nombre = "Mario "
saludo2 = "buenos días."

#CONCATENAR CON +
saludoC = saludo + nombre + saludo2 
# del saludoC -> Esto para borrar datos.

print(saludoC)

#CONCATENAR CON F-STRINGS
saludoC2 = f"Hola {nombre} como estas. Tu edad: {num}" #Buena opción de concatenación. Con el f al inicio.

print(saludoC2)

#OPERADORES DE PERTENENCIA (IN Y NOT IN)
print("Pedro" in saludoC2) #Buscar en una cadena, devuelve True o False 

