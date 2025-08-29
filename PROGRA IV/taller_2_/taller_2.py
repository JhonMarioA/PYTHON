from io import *


# 1. ___________________________________

class Numero:

    entero = 123

    def suma(self):

        total = 0
        numero_lista = list(str(self.entero))

        for i in range(len(numero_lista)):
            total += int(numero_lista[i])

        return total

    def numeros_txt(self):
        archivo = open(r"C:\PROGRAMACIÓN\PYTHON\PROGRA IV\numeros.txt", "w+")
        archivo.write(str(self.entero) + "\n")
        invertido = str(self.entero)[::-1]
        archivo.write(str(invertido))

""" numero = Numero()
numero.numeros_txt()
total = numero.suma()
print(total) 
"""


# 2. ___________________________________  terminar: guardar inf en .txt

class Frase:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor

    @staticmethod
    def cuenta_palabras(lista_objetos, palabra_buscar):
        cantidad = 0
        for objeto in lista_objetos:
            lista_palabras = objeto.texto.split()  # separar por espacios
            for palabra in lista_palabras:
                if palabra == palabra_buscar:
                    cantidad += 1
        print(f"La cantidad de veces que aparece la palabra '{palabra_buscar}' es {cantidad}")


def ingresar_datos_2():
    lista_objetos = []

    for i in range(2):
        texto = input("Ingrese el texto: ")
        autor = input("Ingrese el autor: ")
        nuevo_objeto = Frase(texto, autor)
        lista_objetos.append(nuevo_objeto)
    
    palabra_buscar = input("Ingrese la palabra a buscar: ")
    Frase.cuenta_palabras(lista_objetos, palabra_buscar)

# ingresar_datos_2()



# 3. ___________________________________ terminar


class Cadena:
    def __init__(self, texto):
        self.texto = texto

    lista_cadenas = []

    @staticmethod 
    def llenar_lista():
        for i in range(3):
            texto = input("Ingrese el texto: ")
        cadena = Cadena(texto)
        lista_cadenas.append(cadena)
        return lista_cadenas
    
    @staticmethod
    def imprimir():
        print(lista_cadenas)

Cadena.imprimir(Cadena.llenar_lista())