class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def agregar_ingrediente(self, nombre):
        nuevo = NodoIngrediente(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_ingrediente(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar_ingredientes(self):
        ingredientes = []
        actual = self.cabeza
        while actual:
            ingredientes.append(actual.nombre)
            actual = actual.siguiente
        return ingredientes if ingredientes else "No hay ingredientes."


class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()
        self.siguiente = None
        self.anterior = None

class ListaPostres:
    def __init__(self):
        self.cabeza = None
    
    def agregar_postre(self, nombre, ingredientes):
        nuevo = NodoPostre(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
        
        for ing in ingredientes:
            nuevo.ingredientes.agregar_ingrediente(ing)
        return f"Postre '{nombre}' agregado con éxito."

    def eliminar_postre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                return f"Postre '{nombre}' eliminado con éxito."
            actual = actual.siguiente
        return "El postre no existe."

    def mostrar_ingredientes_postre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual.ingredientes.mostrar_ingredientes()
            actual = actual.siguiente
        return "El postre no existe."

    def agregar_ingrediente_a_postre(self, nombre_postre, ingrediente):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_postre:
                actual.ingredientes.agregar_ingrediente(ingrediente)
                return f"Ingrediente '{ingrediente}' agregado al postre '{nombre_postre}'."
            actual = actual.siguiente
        return "El postre no existe."

    def eliminar_ingrediente_de_postre(self, nombre_postre, ingrediente):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_postre:
                if actual.ingredientes.eliminar_ingrediente(ingrediente):
                    return f"Ingrediente '{ingrediente}' eliminado del postre '{nombre_postre}'."
                return "El ingrediente no existe en el postre."
            actual = actual.siguiente
        return "El postre no existe."

    def eliminar_duplicados(self):
        nombres_vistos = set()
        actual = self.cabeza
        while actual:
            if actual.nombre in nombres_vistos:
                self.eliminar_postre(actual.nombre)
            else:
                nombres_vistos.add(actual.nombre)
            actual = actual.siguiente
        return "Duplicados eliminados."


menu2 = ListaPostres()

print(menu2.agregar_postre("Galletas", ["Harina", "Mantequilla", "Chocolate"]))
print(menu2.agregar_postre("Helado", ["Leche", "Azúcar", "Vainilla"]))

print("Ingredientes de Galletas:", menu2.mostrar_ingredientes_postre("Galletas"))

print(menu2.agregar_ingrediente_a_postre("Galletas", "Canela"))
print("Ingredientes de Galletas después de agregar Canela:", menu2.mostrar_ingredientes_postre("Galletas"))

print(menu2.eliminar_ingrediente_de_postre("Galletas", "Azúcar"))
print("Ingredientes de Galletas después de eliminar Azúcar:", menu2.mostrar_ingredientes_postre("Galletas"))

print(menu2.eliminar_postre("Helado"))
print("Intentando mostrar ingredientes de Helado:", menu2.mostrar_ingredientes_postre("Helado"))
