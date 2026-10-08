#PY0019: Realiza un programa que muestre por consola si un número entero es impar:
#Se ejecutará indefinidamente hasta que el usuario introduzca un número entero impar. 
#Controlará la excepción ValueError que se puede producir en este caso al convertir a entero
#  algo que no es un entero. En este caso también indicará que debe introducir un número impar
#  y volverá a pedirlo.


entero = 0

while entero % 2 == 0:
    try:
        entero=int(input("Introduce un número entero impar: "))
        if entero % 2 == 0: 
            print("El numero es par")
        else :
            print("EL numero es impar")

    except ValueError:
        print("Debes introducir un numero impar")
