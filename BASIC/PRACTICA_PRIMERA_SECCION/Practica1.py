

# A)

# Promedio de horas
curso_Actual = 1.5
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4


# Diferencias de duración

dif_min = 100 - (curso_Actual / otros_cursos_min * 100)
dif_max = 100 - (curso_Actual * 1000 // otros_cursos_max / 10)
dif_promedio = 100 - (curso_Actual / otros_cursos_promedio * 100)

print("____________________________________________________________________________")
print(f"El curso de dalto explica un {dif_min}% más rapido que el más rapido.")
print(f"El curso de dalto explica un {dif_max}% más rapido que el más lento.")
print(f"El curso de dalto explica un {dif_promedio}% más rapido que el promedio.")


crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio // 10)
tiempo_vacio_dalto = 100 - (curso_Actual * 1000 // crudo_dalto // 10)

print("____________________________________________________________________________")
print(f"Un curso promedio elimina solo el {tiempo_vacio_promedio}% del tiempo vacio.")
print(f"Un curso de dalto elimina {tiempo_vacio_dalto}% del tiempo vacio.")

print("____________________________________________________________________________")
print(f"Ver un curso de dalto de 10 horas equivale a ver {otros_cursos_promedio * 100 // curso_Actual / 10} horas de otro curso")
print(f"Ver un curso dede 10 horas equivale a ver {curso_Actual * 100 // otros_cursos_promedio / 10} horas del curso de dalto")
print("____________________________________________________________________________")