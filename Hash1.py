usuarios = [
    {"id": 101, "nombre": "Ana"},
    {"id": 102, "nombre": "Luis"},
    {"id": 103, "nombre": "Carlos"}
]

# Convertimos la lista en un diccionario para buscar por ID
usuarios_dict = {usuario["id"]: usuario for usuario in usuarios}

# Búsqueda
id_busqueda = 102
usuario_encontrado = usuarios_dict.get(id_busqueda)

print(usuario_encontrado)
