

def saludar():
    print("Hola mundo")

saludar()


def saludar2(nombre, sexo): 

    sexo = sexo.lower()
    if (sexo == 'mujer'):
        print("Hola flaca")

    elif (sexo == 'hombre'):
        print("Hola maquina")

    else:
        print("Vos que sos")


saludar2("Juan", "hombr")         # Pasando parametros


def contraseña(num):              # Pasando parametros

    letras = "abcdefghi"
    numero = str(num)
    num = int(numero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 4

    contra = f"{letras[c1]}{letras[c2]}{letras[c3]}{num*4}"
    return contra

Gcontra = contraseña(8)           # Retornando     
print(Gcontra)





