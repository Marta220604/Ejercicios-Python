#Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100. Usa la función sum(colección).
numeros_pares = [i for i in range(0, 101, 2)]
suma = sum(numeros_pares)
print(suma)