def tiene_palabras_repetidas(palabras):
    vistas = set()  # Usamos un conjunto (set) basado en hash
    for palabra in palabras:
        if palabra in vistas:
            return True  # Palabra repetida encontrada
        vistas.add(palabra)
    return False

texto = ["hola", "mundo", "python", "hola"]
print(tiene_palabras_repetidas(texto))  # Devuelve True
