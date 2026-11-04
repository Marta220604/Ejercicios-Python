#reescribe la calculadora de PY0020 usando funciones.

#EJ PY0020


opcion = ""
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a*b

def division (a,b):
    return a/b

while opcion != "salir":
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("Escribe 'salir' para terminar")

    opcion = input("Elige una opción: ")

    match opcion:

        case "salir":
            print("Calculadora cerrada.")

        case "1":
            try:
                numero1 = int(input("Escribe el primer número que quieres sumar: "))
                numero2 = int(input("Escribe el segundo número que quieres sumar: "))

                print(f"La suma es {suma(numero1,numero2):.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case "2":
            try:
                numero1 = int(input("Escribe el primer número que quieres restar: "))
                numero2 = int(input("Escribe el segundo número que quieres restar: "))

                print(f"La resta es {resta(numero1,numero2):.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case "3":
            try:
                numero1 = int(input("Escribe el primer número que quieres multiplicar: "))
                numero2 = int(input("Escribe el segundo número que quieres multiplicar: "))

                print(f"La multiplicación es {multiplicacion(numero1,numero2):.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case "4":
            try:
                numero1 = int(input("Escribe el primer número que quieres dividir: "))
                numero2 = int(input("Escribe el segundo número que quieres dividir: "))

                if numero2 == 0:
                    print("Error: no se puede dividir entre cero.")
                else:
                    print(f"La división es {division(numero1,numero2):.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case _:
            print("Opción no válida.")



