ingreso = 1100
gastos = 700

if ingreso >= 1000:
    if ingreso - gastos > 500:
      print("Estas bien")

    elif ingreso - gastos > 300:
      print("Estas gastando lo necesario")
            
    else:
       print("Estas mal pa")

elif ingreso >= 500:                          # Else if -> elif
    print("Estas en el promedio")

else:
    print("Estas mal")

     