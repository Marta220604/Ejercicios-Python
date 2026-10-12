# Analiza el PY0025. ¿Qué líneas de código se deben cambiar si se usa set? ¿Tendría sentido hacerlo con tuplas?

# En el py0025
lista_paises = ["España", "Argentina", "Perú"]
lista_paises.append(pais_añadir)
lista_paises.count(pais_añadir) >= 1
lista_paises.count(pais_eliminar) == 0

# Como se haria en set 
lista_paises = {"España", "Argentina", "Perú"} 

lista_paises.add(pais_añadir)
pais_añadir in lista_paises
pais_eliminar not in lista_paises


# No seria recomendable hacerlo con tuplas porque son adecuadas cuando queremos almacenar datos que no vamos a modificar. En este ejercicio tenemos que añadir y eliminar países