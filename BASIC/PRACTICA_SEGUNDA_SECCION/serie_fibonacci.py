
# Función de Fibonacci hasta N num


def fibonacci(num):

    a,b = 0,1
    lista_fibo = []

    for i in range(num):
        if b > num: return lista_fibo

        lista_fibo.append(b)
        a,b = b,a+b


resultado = fibonacci(33)
print(resultado)