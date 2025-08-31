

def pedir_datos_usuario():

    print(f"\nBIENVENIDO\nPor favor ingrese la información a consultar:\n")
    nombre_departamento = input("Departamento: ")
    limite_registros = input("Cantidad máxima de registros a mostrar (máx 10000): ")
    if limite_registros >= 10000:
        print("Cantidad de registros invalida.")
        return

    return nombre_departamento, limite_registros