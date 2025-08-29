
def suma(lista):               # Forma no optima

    sumnum = 0

    for numero in lista: 
        sumnum = sumnum + numero;

    return sumnum

suman = suma([2,4,3,1,2])

print(suman)


def suma2 (*numeros):           # Forma optima

    return sum(numeros)

resultado = suma2(2,6,3,2,1,6)
print(resultado)
    