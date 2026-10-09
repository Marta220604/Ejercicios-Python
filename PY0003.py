#Usando listas realiza las siguientes operaciones.:
#Parte A: Parte de una lista vacía de asistentes. Pide nombres por consola y añadelos a la lista hasta que el usuario escriba “fin”.
#Parte B: Muestra cuántas veces aparece un nombre que te indique el usuario.
#Parte C: muestra por consola la primera posición en la que aparece el nombre anterior y elimina esta ocurrencia.
#Parte D: Inserta al inicio (posición 0) un asistente VIP.
#Muestra la lista final.
#Ejemplo:
#Entrada: Juan, Ana, Ana, Luis, fin; consulta “Ana”; VIP “Directora”.
#Salida: count("Ana")=2, index("Ana")=1; tras remove("Ana"): […]; tras insert(0,"Directora"): ["Directora", …]

lista_asistentes = []
entrada = ""

#Parte A
while entrada != "fin":
    entrada = input("Escribe un nombre (escribe fin para terminar): ")

    if entrada == "fin":
        break

    lista_asistentes.append(entrada)

#Parte B
nombre = input("Escribe un nombre para indicar cuantas veces aparece: ")
contador = lista_asistentes.count(nombre)

print(f'count("{nombre}") = {contador}')



#Parte C
indice = lista_asistentes.index(nombre)
print(f'index("{nombre}") = {indice}')

lista_asistentes.remove(nombre)
print("Tras remove:", lista_asistentes)


#PARTE D
lista_asistentes.insert(0, "Directora")


print('tras insert(0,"Directora")', lista_asistentes)