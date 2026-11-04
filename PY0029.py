def fibonacci(n):
    lista = []
    a = 0
    b = 1

    for i in range(n):
        # Añadimos el numero actual (a) a la lista
        lista.append(a)

        # Calculamos el siguiente numero sumando a y b
        siguiente = a + b

        #actualizamos las variables haciendo que a sea el numero que esta en b y b el numero siguiente
        a = b
        b = siguiente

    return lista

print(fibonacci(7))