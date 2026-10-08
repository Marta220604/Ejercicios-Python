#PY0014: Programa que pida 3 números y muestre la media ponderada entre ellos, 15% 
# la primera 35% la segunda y 50% la tercera.
#Se debe controlar la excepción ValueError para saber si es un float lo que han introducido o no. 
#Se mostrará la media ponderada con dos decimales. (:.2f)

numeros = []

try:
    for i in range(0,3): 
        numero = float(input("Escribe un numero: "))
        numeros.append(numero)
except ValueError:
    print("Debes introducir un numero")

media = numeros[0] * 0.15 + numeros[1] * 0.35 + numeros[2] * 0.5

print(f"{media:.2f}")
