
print("Pizzería La Beata")

dinero = float(input("¿Cuánto dinero tienes? "))

precio_margarita = 8.95
precio_barbacoa = 10.50
precio_4_quesos = 9.75

precio_extra_queso = 1.25
precio_jamon = 1.50
precio_champiñones = 0.90

total = 0
pedido = []
pizza = 0
opcion = 0

print("Pizzas disponibles:")
print(f"1. Margarita: {precio_margarita:.2f}€")
print(f"2. Barbacoa: {precio_barbacoa:.2f}€")
print(f"3. Cuatro quesos: {precio_4_quesos:.2f}€")

pizza = int(input("Elige una pizza: "))

match pizza:
    case 1:
        total = precio_margarita
        pedido.append(f"Margarita {precio_margarita:.2f}€")
    case 2:
        total = precio_barbacoa
        pedido.append(f"Barbacoa {precio_barbacoa:.2f}€")
    case 3:
        total = precio_4_quesos
        pedido.append(f"Cuatro quesos {precio_4_quesos:.2f}€")
    case _:
        print("Opción no válida")

if pizza >= 1 and pizza <= 3:
    print(f"Precio actual: {total:.2f}€")
    print(f"Saldo restante: {dinero - total:.2f}€")

    while opcion != 4:
        print("Ingredientes extra:")
        print(f"1. Extra de queso: {precio_extra_queso:.2f}€")
        print(f"2. Jamón: {precio_jamon:.2f}€")
        print(f"3. Champiñones: {precio_champiñones:.2f}€")
        print("4. Terminar de añadir ingredientes")

        opcion = int(input("¿Qué ingrediente quieres añadir? "))

        match opcion:
            case 1:
                total = total + precio_extra_queso
                pedido.append(f"Extra de queso {precio_extra_queso:.2f}€")
            case 2:
                total = total + precio_jamon
                pedido.append(f"Jamón {precio_jamon:.2f}€")
            case 3:
                total = total + precio_champiñones
                pedido.append(f"Champiñones {precio_champiñones:.2f}€")
            case 4:
                opcion = 4
            case _:
                print("Opción no válida")

        print(f"Precio actual: {total:.2f}€")
        print(f"Saldo restante: {dinero - total:.2f}€")

    if dinero >= total:
        print("\n--- Su Pedido ---")
        print(f"El total de su pedido es {total:.2f}€")
        print(f"Su cambio de {dinero:.2f}€ es: {dinero - total:.2f}€")

        for elemento in pedido:
            print(elemento)

        print("\nGracias por su visita")
    else:
        print("No tienes dinero suficiente. Vuelve a empezar.")
