alumnos = [
    {"nombre": "Carlos", "matricula": "A01", "materias": 7, "promedio": 8.5},
    {"nombre": "Ana", "matricula": "A02", "materias": 10, "promedio": 9.0},
    {"nombre": "Luis", "matricula": "A03", "materias": 5, "promedio": 7.2},
]

# a) Ordenar por nombre (Selección directa)
def seleccion_directa(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]["nombre"] < arr[min_idx]["nombre"]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

seleccion_directa(alumnos)
print("Ordenado por nombre:")
for a in alumnos:
    print(a)

# b) Quicksort por número de materias
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x["materias"] <= pivote["materias"]]
        mayores = [x for x in arr[1:] if x["materias"] > pivote["materias"]]
        return quicksort(menores) + [pivote] + quicksort(mayores)

ordenados_por_materias = quicksort(alumnos)
print("\nOrdenado por materias:")
for a in ordenados_por_materias:
    print(a)
