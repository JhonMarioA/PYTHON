# Función de numeros primos de 0 a N


def primo(num):

    for i in range(2, num-1):
        if num%i == 0: return False
    return True


def primos(num):

    lista =  []
    for i in range(2, num+1):
        if primo(i): lista.append(i)
    
    return lista

resultado = primos(13)
print(resultado)

