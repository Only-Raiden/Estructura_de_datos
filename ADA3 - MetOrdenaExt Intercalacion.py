def intercalacion(lista1, lista2):
    resultado = []
    i = j = 0
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado


# Ejemplo de uso
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
print("Resultado de intercalación:", intercalacion(l1, l2))
