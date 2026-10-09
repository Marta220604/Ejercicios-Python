#Dada una lista de precios (floats), por ejemplo, “1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4”), aplica:
#10% de descuento a los elementos de índice par
#20% de descuento a los elementos de índice impar 
#Si el precio es negativo, se saltará ese elemento.
#Actualiza la lista original y ve mostrando por consola los cambios. El formato de salida es: 
#“indice_lista=N, precio_antes=X.XX, precio_después=Y.YY”

lista_precios = [1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4]

for indice in range(len(lista_precios)):

    precio_antes = lista_precios[indice]

    if precio_antes < 0:
        continue

    if indice % 2 == 0:
        precio_despues = precio_antes * (1 - 0.10)
    else:
        precio_despues = precio_antes * (1 - 0.20)

    lista_precios[indice] = precio_despues

    print(f"indice_lista={indice}, precio_antes={precio_antes:.2f}, precio_después={precio_despues:.2f}")
