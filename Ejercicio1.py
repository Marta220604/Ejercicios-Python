#PY0016: Crea bucles que muestren los siguientes rangos de números:
#Del 0 al 20.
for i in range (0,21):
    print(i)

print("\n")

#Números pares del 0 al 20.
for i in range (0,21):
    if i % 2 == 0:
        print(i)

print("\n")

#Números impares del 0 al -20.
for i in range (0,-21,-1):
    if i % 2 != 0:
        print(i)