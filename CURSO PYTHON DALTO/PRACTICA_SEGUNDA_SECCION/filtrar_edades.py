
# Se ingresara el nombre y edad de un N personas, el mayor de ellos será el profesor y el menor de ellos será su asistente.



def agregar_compañeros(num_p):
  
   compañeros = []
  
   for i in range(num_p):

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    print("\n")
    
    compañero = (nombre, edad)
    compañeros.append(compañero)

   compañeros.sort(key = lambda x:x[1])

   asistente = compañeros[0][0]
   profesor = compañeros[-1][0]

   return asistente, profesor

asistente, profesor = agregar_compañeros(4)

print(f"El profesor es: {profesor} y el asistente es: {asistente}")






