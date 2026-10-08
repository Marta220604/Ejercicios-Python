#Al realizar una consulta en un registro, 
# hemos obtenido una cadena de texto corrupta que viene justo al revés. 
# Contiene el nombre de un alumno y la nota de un exámen. 
# En concreto el registro es "zeréP nauJ,01". 
# Crea un programa que le dé la vuelta a la cadena y muestre por 
# consola una cadena como la siguiente:
#{Nombre Apellido} ha sacado un Nota de {nota}.

cadena = "zeréP nauJ,01"

cadena = cadena[::-1]
nota, nombre = cadena.split(",")

print(f"{nombre} ha sacado un Nota de {nota}.")

