# Realiza un programa que siga las siguientes instrucciones:
# Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
# Crea un conjunto llamado administradores con los administradores Juan y Marta.
# Borra al administrador Juan del conjunto de administradores.(discard)
# Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.(add)
# Muestra todos los usuarios por pantalla de forma dinámica (bucle for), además debes indicar si cada usuario es administrador o no.

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.discard("Juan")
administradores.add("Marcos")

for elemento in usuarios:
    if elemento in administradores:
        print(f"{elemento}: es administrador")
    else:
        print(f"{elemento}: no es administrador")