def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        gap //= 2
    return arr


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr


def mostrar_menu():
    print("\n--- MENÚ DE ORDENAMIENTO ---")
    print("1. Shell Sort")
    print("2. Quicksort")
    print("3. Heapsort")
    print("4. Radix Sort")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break

        n = int(input("¿Cuántos números vas a ingresar?: "))
        datos = []
        for _ in range(n):
            numero = int(input("Ingresa un número: "))
            datos.append(numero)
        
        if opcion == '1':
            print("\n--- Shell Sort ---")
            print("Lista ordenada:", shell_sort(datos.copy()))
        elif opcion == '2':
            print("\n--- Quicksort ---")
            print("Lista ordenada:", quicksort(datos.copy()))
        elif opcion == '3':
            print("\n--- Heapsort ---")
            print("Lista ordenada:", heapsort(datos.copy()))
        elif opcion == '4':
            print("\n--- Radix Sort ---")
            print("Lista ordenada:", radix_sort(datos.copy()))
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
