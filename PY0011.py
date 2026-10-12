
# 1. Unir una lista de listas en una sola lista
listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

lista_unida = [numero for lista in listas for numero in lista]

print(lista_unida)


# 2. Unir las listas mostrando solo los números pares
lista_pares = [numero for lista in listas for numero in lista if numero % 2 == 0]

print(lista_pares)


# 3. Crear la traspuesta de una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

traspuesta = [[fila[columna] for fila in matriz] for columna in range(len(matriz))]

print(traspuesta)
