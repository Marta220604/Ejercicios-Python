#PY0033: Realiza un programa que contenga la función "separar_lista(lista)". 
# La función recibe una lista de números enteros ( xej [6, 1, 8, 7, 3, 2, 4, 9, 5])
# Devuelve dos listas ordenadas. La primera con los números pares y la segunda con los números impares. 
# Debes comprobar su funcionamiento con un ejemplo, mostrando el resultado por consola. 
# Comprueba que se ejecuta como main para realizar estos ejemplos
lista = [6, 1, 8, 7, 3, 2, 4, 9, 5]
def separar_lista(lista):

    listaPar = []
    listaImpar = []

    for x in lista:
        if x % 2 == 0:
            listaPar.append(x)
        else: 
            listaImpar.append(x)

    listaPar.sort()
    listaImpar.sort()

    return listaPar, listaImpar

#comprobacion de que se ejecuta como main 
if __name__ == "__main__":
    print(separar_lista(lista))