# Jhon Mario Aguirre - Taller 3, Programación IV

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


libro1 = Libro("MMM", "Joung", 2022, "hkj", "comedia")
libro2 = Libro("UUU", "Lebron Gabriel", 2016, "nls", "romance")
Libro.mostrar()

    
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
        with open("estudiantes.txt" "a") as file:
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

Estudiante("Juan", 10212, "Ingeniería en sistemas", "18", 3.5)
Estudiante.promedio()


# 3. ________________________________________________


class InventarioProducto():

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def guardar()

