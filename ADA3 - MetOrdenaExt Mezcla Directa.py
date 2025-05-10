def mezcla_directa(arr):
    if len(arr) <= 1:
        return arr

    def intercalar(a, b):
        resultado = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                resultado.append(a[i])
                i += 1
            else:
                resultado.append(b[j])
                j += 1
        resultado += a[i:]
        resultado += b[j:]
        return resultado

    mid = len(arr) // 2
    izquierda = mezcla_directa(arr[:mid])
    derecha = mezcla_directa(arr[mid:])
    return intercalar(izquierda, derecha)


# Ejemplo
lista = [12, 5, 8, 3, 1, 7]
print("Resultado:", mezcla_directa(lista))
