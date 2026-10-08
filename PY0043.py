
cadena = input("Introduce una cadena: ")

cadena = cadena.lower()

caracteres_contados = ""

for caracter in cadena:

    if caracter != " ":

        
        encontrado = False

        for caracter2 in caracteres_contados:

           
            if caracter == caracter2:
                encontrado = True

        if encontrado == False:

            contador = 0


            for caracter2 in cadena:

               
                if caracter == caracter2:
                    contador += 1

            print(caracter, ":", contador)

            caracteres_contados += caracter