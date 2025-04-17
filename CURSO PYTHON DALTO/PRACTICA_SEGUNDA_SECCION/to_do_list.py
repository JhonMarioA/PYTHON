
tareas = []  # Lista de diccionarios


def agregar_tarea():
    nombre = input("Ingrese el nombre de la nueva tarea: ")
    tarea = {"nombre": nombre, "completado": False}
    tareas.append(tarea)
    print("✅ Tarea agregada correctamente.")


def mostrar_tareas():
    if not tareas:
        print("📭 No hay tareas registradas.")
        return

    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔️ Completada" if tarea["completado"] else "❌ Pendiente"
        print(f"{i}. {tarea['nombre']} - {estado}")


def completar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completado"] = True
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ Número de tarea no válido.")
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número.")


def eliminar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"🗑️ Tarea '{tarea_eliminada['nombre']}' eliminada.")
        else:
            print("❌ Número de tarea no válido.")
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número.")


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_tarea()
            case "2":
                mostrar_tareas()
            case "3":
                completar_tarea()
            case "4":
                eliminar_tarea()
            case "5":
                print("👋 Saliendo del gestor de tareas.")
                break
            case _:
                print("⚠️ Opción no válida. Intente de nuevo.")


# Iniciar programa
menu()



