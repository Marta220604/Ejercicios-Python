#Crea una calculadora que haga las operaciones de sumar multiplicar dividir y restar de dos números enteros introducidos por teclado. 
#El resultado se dará en dos decimales. 
#Debe ofrecerse el menú mientras el usuario no escriba “salir”. Dará igual que sea mayúsculas o minúsculas o que tenga espacios por delante y por detrás.
#Controlar que son números enteros los que se mete. 
#Controlar que la división por cero es un error.

opcion = ""

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

                print(f"La suma es {numero1 + numero2:.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case "2":
            try:
                numero1 = int(input("Escribe el primer número que quieres restar: "))
                numero2 = int(input("Escribe el segundo número que quieres restar: "))

                print(f"La resta es {numero1 - numero2:.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case "3":
            try:
                numero1 = int(input("Escribe el primer número que quieres multiplicar: "))
                numero2 = int(input("Escribe el segundo número que quieres multiplicar: "))

                print(f"La multiplicación es {numero1 * numero2:.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case "4":
            try:
                numero1 = int(input("Escribe el primer número que quieres dividir: "))
                numero2 = int(input("Escribe el segundo número que quieres dividir: "))

                if numero2 == 0:
                    print("Error: no se puede dividir entre cero.")
                else:
                    print(f"La división es {numero1 / numero2:.2f}")

            except ValueError:
                print("Error: debes introducir números enteros.")

        case _:
            print("Opción no válida.")