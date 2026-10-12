
inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}

ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']

reposiciones = {'CUS002': 10, 'CUS004': 7}


# 1. Crear una copia del inventario
inventario = inventario_inicial.copy()


# 2. Procesar las ventas
avisos = []

for codigo in ventas:

    if codigo not in inventario:
        inventario.setdefault(codigo, 0)
        avisos.append("El producto " + codigo + " no existía en el inventario")

    inventario[codigo] = inventario.get(codigo, 0) - 1


# Mostrar los avisos
for aviso in avisos:
    print(aviso)


# 3. Aplicar las reposiciones
for codigo, cantidad in reposiciones.items():

    if codigo in inventario:
        inventario[codigo] = inventario[codigo] + cantidad
    else:
        inventario[codigo] = cantidad


# 4. Generar el informe
print("\nNúmero de referencias:", len(inventario))
print("Unidades totales:", sum(inventario.values()))


# 5. Eliminar productos con stock 0 o negativo
claves_a_borrar = []

for codigo, stock in inventario.items():
    if stock <= 0:
        claves_a_borrar.append(codigo)

for codigo in claves_a_borrar:
    inventario.pop(codigo)


print("\nInventario final:", inventario)


# 6. Consultar el stock de un producto
codigo = input("\nIntroduce el código del producto que quieres consultar: ")

if codigo in inventario:
    print("Stock:", inventario[codigo])
else:
    print("No existe")


# 7. Borrar el diccionario
del inventario
