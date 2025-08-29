"""
Nivel 3: Estructuras de Datos
Lista de Compras:

Crea una lista con 3 productos. Luego, permite al usuario agregar más productos, eliminar uno y ver la lista actualizada.
"""

lista1 = ["Leche", "Carne", "Galletas"]

def ingresarP():
    nuevoP = input("Ingrese el nuevo producto: ")
    lista1.append(nuevoP)
    print("\nProducto ingresado correctamente.")

def eliminarP():
    productoE = input("Ingrese el producto a eliminar: ")
    if productoE in lista1:
        lista1.remove(productoE)
        print("\nElemento eliminado correctamente.")
    else:
        print("\nEl producto no está en la lista.")

def mostrarP():
    print("\nLista actualizada:")
    print(lista1)

def main():
    while True:
        print("\nMENU:")
        print("1) Agregar más productos.")
        print("2) Eliminar un producto.")
        print("3) Mostrar lista actualizada.")
        print("4) Salir.")

        opc = input("Ingrese la opción: ")

        match opc:
            case "1":
                ingresarP()
            case "2":
                eliminarP()
            case "3":
                mostrarP()
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

main()
