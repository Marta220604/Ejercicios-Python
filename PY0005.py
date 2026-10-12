
inscritos = {"Marta", "Antonio", "David", "Itziar"}

# 1. Dar de alta nuevos inscritos hasta escribir fin
persona = ""

while persona != "fin":
    persona = input("Escribe un nombre (fin para terminar): ")

    if persona == "fin":
        print("Fin del registro")
    elif persona == "" or persona != persona.strip():
        print("Escribe un nombre válido")
    else:
        inscritos.add(persona)


# 2. Dar de alta varios usuarios a la vez
nombres = input("Escribe varios nombres separados por comas: ")

lista_nombres = nombres.split(",")

nuevos_inscritos = set()

for nombre in lista_nombres:
    nombre = nombre.strip()

    if nombre != "":
        nuevos_inscritos.add(nombre)

inscritos.update(nuevos_inscritos)


# 3. Crear una copia del conjunto
copia_inscritos = inscritos.copy()

print("Copia de los inscritos:", copia_inscritos)


# 4. Dar de baja a un inscrito
persona = input("Escribe el nombre que quieres dar de baja: ").strip()

try:
    inscritos.remove(persona)
    print("Inscrito eliminado correctamente")
except:
    print("Esa persona no está inscrita")


# 5. Consultar si una persona está inscrita
persona = input("Escribe un nombre para comprobar si está inscrito: ").strip()

if persona in inscritos:
    print(persona, "está inscrito")
else:
    print(persona, "no está inscrito")


# 6. Consultar si alguien de un grupo está inscrito
grupo = {"Marta", "Pedro", "Lucía", "Antonio"}

print("Personas del grupo que están inscritas:")

for persona in grupo:
    if persona in inscritos:
        print(persona)


# 7. Mostrar el número total de inscritos y la lista ordenada
print("Número total de inscritos:", len(inscritos))

print("Lista de inscritos ordenada alfabéticamente:")

for persona in sorted(inscritos):
    print(persona)
