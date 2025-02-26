def capturar_nombres(tamaño):
    nombres = []
    longitudes = []
    for i in range(tamaño):
        nombre = input(f"Ingresa el nombre {i+1}: ")
        nombres.append(nombre)
        longitudes.append(len(nombre))
    return nombres, longitudes

def mostrar_resultados(nombres, longitudes):
    for i in range(len(nombres)):
        print(f"Nombre: {nombres[i]}, Longitud: {longitudes[i]}")

def main():
    tamaño = int(input("Ingrese el tamaño de los arreglos: "))
    nombres, longitudes = capturar_nombres(tamaño)
    mostrar_resultados(nombres, longitudes)

if __name__ == "__main__":
    main()