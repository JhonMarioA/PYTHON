
# (Forma no optima)

# archivo_sin_leer = open("BASIC\\Archivos\\arc.txt", encoding="UTF-8")
# archivo = archivo_sin_leer.read()

# print(archivo)


# (Forma optima)
with open("BASIC/Archivos/arc.txt", encoding="UTF-8") as archivo_sin_leer:
    archivo = archivo_sin_leer.read()

print(archivo)

