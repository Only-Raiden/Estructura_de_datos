alumnos = [
    {"nombre": "Carlos", "promedio": 8.2, "materias": 6},
    {"nombre": "Ana", "promedio": 9.1, "materias": 10},
    {"nombre": "Luis", "promedio": 7.8, "materias": 8},
]

# a) Búsqueda lineal en desordenado
def buscar_lineal(nombre, arreglo):
    for alumno in arreglo:
        if alumno["nombre"] == nombre:
            return alumno
    return None

# b) Búsqueda binaria en ordenado
def buscar_binaria(nombre, arreglo):
    inicio = 0
    fin = len(arreglo) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arreglo[medio]["nombre"] == nombre:
            return arreglo[medio]
        elif arreglo[medio]["nombre"] < nombre:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

# Prueba
nombre_buscado = "Ana"

print("\nBúsqueda lineal:")
resultado = buscar_lineal(nombre_buscado, alumnos)
print(resultado if resultado else "Alumno no encontrado.")

print("\nBúsqueda binaria:")
alumnos_ordenados = sorted(alumnos, key=lambda x: x["nombre"])
resultado = buscar_binaria(nombre_buscado, alumnos_ordenados)
print(resultado if resultado else "Alumno no encontrado.")
