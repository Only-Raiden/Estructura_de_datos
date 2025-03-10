# Definimos la clase Pila
class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad  # Capacidad máxima de la pila
        self.pila = []             # Lista para representar la pila
        self.tope = 0              # Inicialmente el tope es 0

    # Método para insertar un elemento en la pila
    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.pila.append(elemento)
            self.tope += 1
            print(f"Insertar({elemento}): {self.pila}, TOPE={self.tope}")
        else:
            print(f"Error: Desbordamiento al intentar insertar {elemento}. La pila está llena.")

    # Método para eliminar un elemento de la pila
    def eliminar(self):
        if self.tope > 0:
            elemento_eliminado = self.pila.pop()
            self.tope -= 1
            print(f"Eliminar(): {self.pila}, TOPE={self.tope}")
            return elemento_eliminado
        else:
            print("Error: Subdesbordamiento al intentar eliminar. La pila está vacía.")
            return None

# Función principal para realizar las operaciones y mostrar los resultados
def main():
    # Crear una pila con capacidad máxima de 8 elementos
    capacidad_maxima = 8
    pila = Pila(capacidad_maxima)

    # Realizar las operaciones dadas en el problema
    print("Estado inicial de la pila:", pila.pila, f"TOPE={pila.tope}")
    
    pila.insertar("X")  # a. Insertar X
    pila.insertar("Y")  # b. Insertar Y
    pila.eliminar()     # c. Eliminar Z (elimina el tope actual)
    pila.eliminar()     # d. Eliminar T (elimina el siguiente tope)
    pila.eliminar()     # e. Eliminar U (intenta eliminar pero la pila ya está vacía)
    pila.insertar("V")  # f. Insertar V
    pila.insertar("W")  # g. Insertar W
    pila.eliminar()     # h. Eliminar p (elimina el tope actual)
    pila.insertar("R")  # i. Insertar R

    # Mostrar el estado final de la pila y cuántos elementos tiene
    print("\nEstado final de la pila:", pila.pila, f"TOPE={pila.tope}")
    print(f"La pila quedó con {pila.tope} elementos.")

if __name__ == "__main__":
    main()
