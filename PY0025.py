
lista_paises = ["España", "Argentina", "Perú"]
opcion = 0
numero_ejecuciones = 0

while opcion!= 5:

    try:
        opcion = int(input("MENÚ. Elija una de las siguientes opciones marcando su número: \n"
            "1. Imprimir alfabéticamente en orden ascendente\n"
            "2. Imprimir alfabéticamente en orden descendente\n"
            "3. Añadir País\n"
            "4. Eliminar Pais\n"
            "5. Salir\n"))
    except ValueError:
        print("Error, debes introducir un número entero")
        numero_ejecuciones = numero_ejecuciones + 1
        print(f"Numero de ejecuciones del menu: {numero_ejecuciones}")
        continue
    
    


    match opcion:
        case 1:
            numero_ejecuciones = numero_ejecuciones + 1
            print(sorted(lista_paises))
            print(f"Numero de ejecuciones del menu: {numero_ejecuciones}")
            print("#" * 70 + "\n\n")
        case 2:
            numero_ejecuciones = numero_ejecuciones + 1
            print(sorted(lista_paises)[::-1])
            print(f"Numero de ejecuciones del menu: {numero_ejecuciones}")
            print("#" * 70 + "\n\n")
        case 3:
            numero_ejecuciones = numero_ejecuciones + 1
            pais_añadir=""
            if len(lista_paises) == 6:
                print("Tamaño maximo de la lista alcanzado, no se puede añadir mas paises")
            else:
                while pais_añadir == "":
                    pais_añadir= input("Escribe el pais que quieres añadir: ")
                    if pais_añadir == "":
                        print("Error, escribe un pais")

                pais_añadir = pais_añadir[0].upper() + pais_añadir[1:].lower()

                if lista_paises.count(pais_añadir)>=1:
                    print("Ese pais ya esta en la lista")
                else:
                    lista_paises.append(pais_añadir)
                    print("Operacion realizada")
                    print(lista_paises)
                    print("#" * 70 + "\n\n")

            print(f"Numero de ejecuciones del menu: {numero_ejecuciones}")

            

        case 4:
            numero_ejecuciones = numero_ejecuciones + 1
            pais_eliminar =""
            while pais_eliminar == "":
                pais_eliminar= input("Escribe el pais que quieres eliminar: ")
                if pais_eliminar == "":
                    print("Error, escribe un pais")
            
            pais_eliminar = pais_eliminar[0].upper() + pais_eliminar[1:].lower()

            if lista_paises.count(pais_eliminar)==0:
                print("Ese pais no esta en la lista")
            else:
                lista_paises.remove(pais_eliminar)
                print("Operacion realizada")
                print(lista_paises)
                print("#" * 70 + "\n\n")
                
            print(f"Numero de ejecuciones del menu: {numero_ejecuciones}")
            

        case 5:
            numero_ejecuciones = numero_ejecuciones + 1
            print("Muchas gracias")
            print(f"Numero total de intentos: {numero_ejecuciones}")
            print("Un saludo")
            break

        case _:
            numero_ejecuciones = numero_ejecuciones + 1
            print("Escribe una opción válida")

        
            