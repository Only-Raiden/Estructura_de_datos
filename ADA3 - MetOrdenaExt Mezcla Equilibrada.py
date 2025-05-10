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


def mezcla_equilibrada_simulada(lista):
    mitad = len(lista) // 2
    parte1 = sorted(lista[:mitad])
    parte2 = sorted(lista[mitad:])
    return intercalacion(parte1, parte2)


# Ejemplo de uso
lista_grande = [42, 7, 15, 23, 4, 89, 34, 2]
print("Resultado de mezcla equilibrada:", mezcla_equilibrada_simulada(lista_grande))
