
import modulo_saludar  # Se importa el modulo con la función (Nombre del archivo sin el .py)

# from modulo_saludar import saludar      -> Esto para importar solo una función en especificos, al llamarla solo se llama la función, ya no como metodo
# Se puede importar varias funciones con comas, ej: saludar, saludar raro, ...

# import modulo_saludar as saludito    -> Podemos referirnos de otra manera a un modulo cambiandole el "nombre" por medio del "as"

# from modulo_saludar import *   -> Lo usamos para importar todas las funciones (MUY MALA PRACTICA, gasta muchos recursos)


saludo = modulo_saludar.saludar("Mario")     # Llamamos a la función como un metodo

print(saludo)


