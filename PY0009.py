
palabras = ["python", "java   ", "javascript", "go", "rust", "", ""]


# 1. Diccionario con la palabra y su longitud
diccionario1 = {palabra.strip(): len(palabra.strip()) for palabra in palabras}

print(diccionario1)


# 2. Lo mismo, pero eliminando las cadenas vacías
diccionario2 = {palabra.strip(): len(palabra.strip()) for palabra in palabras if palabra.strip() != ""}

print(diccionario2)


# 3. Mayúsculas si la longitud es mayor que 5 y minúsculas en otro caso
diccionario3 = {
    palabra.strip().upper() if len(palabra.strip()) > 5 else palabra.strip().lower(): len(palabra.strip())
    for palabra in palabras
    if palabra.strip() != ""
}

print(diccionario3)
