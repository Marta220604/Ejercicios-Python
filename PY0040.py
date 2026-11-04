#PY0040: mostrar por pantalla el área de una circunferencia.  area = pi*radio2
#Pide el radio por consola.
#Usa una función lambda que reciba el argumento radio.
#Usa la librería math para pi
#muestra el resultado con dos decimales.



import math

#Pedimos el radio por consola y lo asignamos a la variable radio
radio = float(input("Introduce el radio: "))

#usamos funcion lambda para calcular el area
area = lambda radio: math.pi * radio**2


#llamamos a la funcion area creada antes y lo imprimimpos por pantalla 
print(f"El área es: {area(radio):.2f}")