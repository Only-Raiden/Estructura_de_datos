A1 = [{"nombre": "Andrés", "presentaciones": 3, "fechas": ["2023-01-10", "2023-02-10", "2023-03-10"]}]
A2 = [{"nombre": "Carlos", "presentaciones": 2, "fechas": ["2024-01-01", "2024-02-01"]}]
A3 = [{"nombre": "Beatriz", "presentaciones": 4, "fechas": ["2025-01-05", "2025-01-12", "2025-02-20", "2025-03-15"]}]

# Intercalación
def intercalar(*archivos):
    resultado = []
    for archivo in archivos:
        resultado.extend(archivo)
    return sorted(resultado, key=lambda x: x["nombre"])

RECITALES = intercalar(A1, A2, A3)
print("Archivo RECITALES:")
for r in RECITALES:
    print(r)
