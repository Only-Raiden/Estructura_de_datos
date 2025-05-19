def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Lista desordenada
numeros = [23, 12, 45, 67, 89, 10, 33]
objetivo = 67

resultado = busqueda_secuencial(numeros, objetivo)
if resultado != -1:
    print(f"El número {objetivo} se encontró en el índice {resultado}")
else:
    print("Número no encontrado")
