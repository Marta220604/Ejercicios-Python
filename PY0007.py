import copy

# Datos iniciales
calificaciones = [
    {"alumno": "Ana", "modulo": "Programación", "nota": 7.5},
    {"alumno": "Luis", "modulo": "Sistemas", "nota": 6.0},
    {"alumno": "Ana", "modulo": "Sistemas", "nota": 8},
    {"alumno": "Marta", "modulo": "Programación", "nota": 9.0},
    {"alumno": "Marta", "modulo": "Sistemas", "nota": 10.0}
]


# 1. Crear el diccionario alumnos
alumnos = {}

for dato in calificaciones:
    alumno = dato["alumno"]
    modulo = dato["modulo"]
    nota = dato["nota"]

    alumnos.setdefault(alumno, {})
    alumnos[alumno].setdefault(modulo, [])
    alumnos[alumno][modulo].append(nota)

print("ALUMNOS:")
print(alumnos)


# 2. Calcular la media de cada alumno
medias_alumnos = {}

for alumno, modulos in alumnos.items():
    notas_maximas = []

    for modulo, notas in modulos.items():
        if len(notas) > 0:
            notas_maximas.append(max(notas))

    if len(notas_maximas) > 0:
        media = sum(notas_maximas) / len(notas_maximas)
        medias_alumnos[alumno] = media

print("\nMEDIA DE CADA ALUMNO:")
print(medias_alumnos)


# 3. Crear un diccionario con la nota máxima de cada módulo y alumno
maximas_modulos = {}

for alumno, modulos in alumnos.items():
    for modulo, notas in modulos.items():

        nota_maxima = max(notas)

        maximas_modulos.setdefault(modulo, {})
        maximas_modulos[modulo][alumno] = nota_maxima

print("\nNOTAS MÁXIMAS POR MÓDULO:")
print(maximas_modulos)


# 4. Filtrar aprobados por módulo
aprobados = {}

for modulo, notas_alumnos in maximas_modulos.items():
    aprobados[modulo] = {
        alumno: nota
        for alumno, nota in notas_alumnos.items()
        if nota >= 5
    }

print("\nAPROBADOS POR MÓDULO:")
print(aprobados)


# 5. Aplicar correcciones a las últimas notas
correcciones = {
    "Ana": {"Programación": +0.75}
}

alumnos_corregidos = copy.deepcopy(alumnos)

for alumno, modulos in correcciones.items():

    for modulo, correccion in modulos.items():

        if alumno in alumnos_corregidos:
            if modulo in alumnos_corregidos[alumno]:

                notas = alumnos_corregidos[alumno][modulo]
                notas[-1] = notas[-1] + correccion

print("\nALUMNOS CON CORRECCIONES:")
print(alumnos_corregidos)


# 6. Eliminar una nota concreta
alumno = input("\nAlumno del que quieres eliminar una nota: ")
modulo = input("Módulo: ")
indice = int(input("Índice de la nota que quieres eliminar (empieza en 0): "))

if alumno in alumnos:
    if modulo in alumnos[alumno]:

        notas = alumnos[alumno][modulo]

        if indice >= 0 and indice < len(notas):

            nota_eliminada = notas.pop(indice)

            print("Nota eliminada:", nota_eliminada)

            if len(notas) == 0:
                alumnos[alumno].pop(modulo)

            if len(alumnos[alumno]) == 0:
                alumnos.pop(alumno)

        else:
            print("Ese índice no existe")

    else:
        print("Ese módulo no existe")

else:
    print("Ese alumno no existe")

print("\nALUMNOS DESPUÉS DE ELIMINAR LA NOTA:")
print(alumnos)
