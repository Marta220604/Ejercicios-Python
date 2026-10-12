# 1. Crear una lista con los cuadrados del 1 al 20
cuadrados = [numero ** 2 for numero in range(1, 21)]

print(cuadrados)

# 2. Filtrar los cuadrados para que solo queden los impares
impares = [numero for numero in cuadrados if numero % 2 != 0]

print(impares)