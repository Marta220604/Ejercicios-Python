# Dada una lista con un número variable de cadenas, que pueden indicar
#  por ejemplo las tareas del hogar que hay que realizar o los platos de un menú. 
# Imprime cada elemento de esta lista precedido por su número, empezando en 1. Por ejemplo:
#1. Limpiar
#2. Comprar Comida
#3. Salir
lista_tareas = ["Limpiar", "Comprar comida", "Salir"]

numero = 1

for tarea in lista_tareas:
    print(numero, ". ", tarea)
    numero += 1