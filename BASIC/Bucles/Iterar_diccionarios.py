
diccionario = {
    "Nombre" : "Mario",
    "Edad": 18,
    "Clave": 88
}

# recorriendo para optener claves
for key in diccionario:
    print(key) 

# recorriendo un diccionario con items
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es {key} y el valor es {value}")


