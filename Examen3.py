empleados = [
    {"nombre": "Carlos", "estado_civil": "Soltero", "antigüedad": 5, "categoria": "A", "sueldo": 15000},
    {"nombre": "Ana", "estado_civil": "Casado", "antigüedad": 2, "categoria": "B", "sueldo": 12000},
    {"nombre": "Luis", "estado_civil": "Soltero", "antigüedad": 3, "categoria": "A", "sueldo": 14000},
]

# a) Mezcla directa (Merge sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        izq = merge_sort(arr[:mid])
        der = merge_sort(arr[mid:])

        return merge(izq, der)
    return arr

def merge(left, right):
    resultado = []
    while left and right:
        if left[0]["nombre"] < right[0]["nombre"]:
            resultado.append(left.pop(0))
        else:
            resultado.append(right.pop(0))
    resultado.extend(left or right)
    return resultado

ordenado_directa = merge_sort(empleados)
print("Mezcla directa:")
for e in ordenado_directa:
    print(e)

# b) Mezcla equilibrada (se simula igual, pero en práctica se hace con archivos en cinta)
ordenado_equilibrada = merge_sort(empleados)  # Simulación
print("\nMezcla equilibrada:")
for e in ordenado_equilibrada:
    print(e)
