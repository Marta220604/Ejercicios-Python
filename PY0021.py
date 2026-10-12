numeros = [10, 15, 100, 40, 35, 353, 400, 40, 500, 420, 340, 115]

resultado = sorted([numero for numero in numeros if numero != 40 and numero <= 339])

print(resultado)