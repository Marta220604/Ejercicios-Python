# Usando listas realiza las siguientes operaciones
# Parte de un menú base: ["Ensalada", "Sopa", "Pasta"].
# Haz una copia independiente llamada menu_hoy.
# Extiende menu_hoy con los especiales: ["Pescado", "Postre"].
# Retira el último plato añadido por error.
# Elimina “Sopa” si está.
# Escoge una posición del menú y eliminala.
# Muestra el menú al revés.
# Vacía por completo la lista base original y demuestra que menu_hoy no se ha visto afectada

menu_base = ["Ensalada", "Sopa", "Pasta"]

menu_hoy= menu_base.copy()

menu_hoy.append("Pescado")
menu_hoy.append("Postre")

menu_hoy.pop(len(menu_hoy) - 1)

if(menu_hoy.count("Sopa")>=1):
    menu_hoy.remove("Sopa")

menu_hoy.pop(1)

print(menu_hoy[::-1])

menu_base.clear()

print(menu_hoy)
print(menu_base)
