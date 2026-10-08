import time

cadena = input("Introduce una cadena: ")

caracter1 = input("Introduce el carácter que quieres sustituir: ")

caracter2 = input("Introduce el carácter por el que quieres sustituirlo: ")

print("\t")

if len(caracter1) != 1 or len(caracter2) != 1:

    print("Error: debes introducir solamente un carácter.")

    time.sleep(3)

else:

    cadena = cadena.replace(caracter1, caracter2)

    print("Cadena modificada:", cadena)