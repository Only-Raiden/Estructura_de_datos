def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Lista ordenada alfabéticamente
palabras = ["abeja", "barco", "cielo", "dado", "elefante", "foca", "gato"]
objetivo = "dado"

resultado = busqueda_binaria(palabras, objetivo)
if resultado != -1:
    print(f"La palabra '{objetivo}' se encontró en el índice {resultado}")
else:
    print("Palabra no encontrada")
