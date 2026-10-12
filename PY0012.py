lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

combinaciones = [(numero1, numero2) for numero1 in lista1 for numero2 in lista2 if (numero1 + numero2) % 2 == 0]

print(combinaciones)