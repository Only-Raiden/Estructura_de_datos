def burbuja(lista, ascendente=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascendente and lista[j] > lista[j+1]) or (not ascendente and lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numeros)
print("Orden ascendente:", burbuja(numeros.copy(), ascendente=True))
print("Orden descendente:", burbuja(numeros.copy(), ascendente=False))
def insercion(lista, ascendente=True):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and ((ascendente and lista[j] > actual) or (not ascendente and lista[j] < actual)):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Uso
nombres = ["Carlos", "Ana", "Luis", "Beatriz", "Miguel"]
print("Original:", nombres)
print("Orden ascendente:", insercion(nombres.copy(), ascendente=True))
print("Orden descendente:", insercion(nombres.copy(), ascendente=False))
def seleccion(lista, ascendente=True):
    n = len(lista)
    for i in range(n):
        idx_extremo = i
        for j in range(i+1, n):
            if (ascendente and lista[j] < lista[idx_extremo]) or (not ascendente and lista[j] > lista[idx_extremo]):
                idx_extremo = j
        lista[i], lista[idx_extremo] = lista[idx_extremo], lista[i]
    return lista

# Uso
calificaciones = [85, 92, 78, 96, 88]
print("Original:", calificaciones)
print("Orden ascendente:", seleccion(calificaciones.copy(), ascendente=True))
print("Orden descendente:", seleccion(calificaciones.copy(), ascendente=False))
