# Jhon Mario Aguirre - Taller 3, Programación IV
import os

# 1. ___________________________________________

class Libro():
    
    def __init__(self, titulo, autor, año, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.editorial = editorial
        self.genero = genero
        self.guardar()

    def guardar(self):
        with open("libros.txt", "a") as file:
            file.write(f"{self.titulo}, {self.autor}, {self.año}, {self.editorial}, {self.genero} \n")

    @staticmethod
    def mostrar():
        autor_buscar = input("Ingrese el autor a buscar: ")

        with open("libros.txt", "r") as file:
            for linea in file:
                str(linea)
                datos = linea.strip().split(",")

                if autor_buscar in datos:
                    print(f"Libros del autor {autor_buscar}:\n {linea}")

"""
libro1 = Libro("MMM", "Joung", 2022, "hkj", "comedia")
libro2 = Libro("UUU", "Lebron Gabriel", 2016, "nls", "romance")
Libro.mostrar()
"""
    
# 2. _____________________________________________

class Estudiante():

    def __init__(self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio
        self.guardar()

    def guardar(self):
        with open("estudiantes.txt", "a") as file:
            file.write(f"{self.nombre}, {self.codigo}, {self.carrera}, {self.edad}, {self.promedio} \n")

    @staticmethod    
    def promedio():

        with open("estudiantes.txt", "r") as file:
            for linea in file:

                datos = linea.strip().split(",")

                if float(datos[4]) >= 3.0:
                    print("Haz aprobado!!!")

                else:
                    print("Haz desaprobado!!!")

""""
Estudiante("Juan", 10212, "Ingeniería en sistemas", "18", 3.5)
Estudiante.promedio()
"""

# 3. ________________________________________________


class InventarioProducto():

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.guardar()

    def guardar(self):
        with open("inventario.txt", "a") as file:
            file.write(f"{self.nombre}, {self.precio}, {self.cantidad}\n")

    @staticmethod
    def valor_inventario():

        valor_inventario = 0

        with open("inventario.txt", "r") as file:
            for linea in file:

                datos = linea.strip().split(",")
                print(datos)
                valor_inventario += (int(datos[1]) * int(datos[2]))
                print(valor_inventario)
""""
producto1 = InventarioProducto("arroz", 5000, 10)
producto2 = InventarioProducto("azucar", 3000, 12)
InventarioProducto.valor_inventario()
"""

# 4. ______________________________________________


class Vehiculo():

    def __init__(self, marca, modelo, año, tipo, placa):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
        self.placa = placa
        self.guardar()

    def guardar(self):
        if self.año == 2025:
            with open("vehiculos.txt", "a") as file:
                file.write(f"{self.marca}, {self.modelo}, {self.año}, {self.tipo}, {self.placa}\n")
    @staticmethod
    def mostrar():
        if os.path.exists("vehiculos.txt"):
            with open("vehiculos.txt", "r") as file:
                print(f"vehiculos registrados del año actual: ")
                for linea in file:
                    print(linea)
        else:
            print("Aún no hay registros.\n")
            return

vehiculo1 = Vehiculo("kjdf", 2025, 2025, "kdfd", "ljan")
vehiculo2 = Vehiculo("nmap", 2016, 2016, "qsc", "bnd")
Vehiculo.mostrar()


# 5. _________________________________________________










                



        


