def binary_search_partitions(l, n):
    """
    Implementa el algoritmo de búsqueda binaria y cuenta la cantidad de particiones realizadas.
    Parámetros:
    - l: Lista de números enteros.
    - n: Número a buscar en la lista.

    Retorna:
    - Cantidad de particiones realizadas antes de encontrar (o no) el número.
    """
    #La lista para aplicar la búsqueda binaria
    l.sort()
    left = 0
    right = len(l) - 1
    partitions = 0  # Contador de particiones

    while left <= right:
        partitions += 1  # Incrementamos el contador de particiones
        mid = (left + right) // 2  # Punto medio

        if l[mid] == n:
            # Si encontramos el número, retorna la cantidad de particiones
            return partitions
        elif l[mid] < n:
            # Si el número es mayor, busca en la mitad derecha
            left = mid + 1
        else:
            # Si el número es menor, busca en la mitad izquierda
            right = mid - 1

    # Si el número no está en la lista: retornamos la cantidad de particiones realizadas
    return partitions

def solution(l, n):
    try:
        # Verificamos que la lista
        if not l:
            raise ValueError("La lista no debe estar vacía.")

        return binary_search_partitions(l, n)

    except Exception as e:
        print(f"Error: {e}")
        return 0  # En caso de error, retornamos 0

#2/5
# Casos de prueba
print(solution([1, 2, 3, 4, 5], 4))  # Salida esperada: 1
print(solution([16, 6, 49, 43, 81], 73))  # Salida esperada: 3
print(solution([32, 60, 2, 6, 44], 44))  # Salida esperada: 2
print(solution([79, 21, 45, 77, 30], 28))  # Salida esperada: 2
print(solution([1], 1))  # Salida esperada: 0
