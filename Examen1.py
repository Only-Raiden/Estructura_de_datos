from operator import itemgetter

hoteles = [
    {"nombre": "Hotel Azul", "ciudad": "Mérida", "estrellas": 4, "cuartos": 120},
    {"nombre": "Hotel Sol", "ciudad": "Cancún", "estrellas": 5, "cuartos": 200},
    {"nombre": "Hotel Luna", "ciudad": "Mérida", "estrellas": 3, "cuartos": 80},
    {"nombre": "Hotel Arena", "ciudad": "Cancún", "estrellas": 4, "cuartos": 150},
]

# Ordenar por ciudad y luego por nombre
hoteles_ordenados = sorted(hoteles, key=itemgetter("ciudad", "nombre"))

for h in hoteles_ordenados:
    print(h)
