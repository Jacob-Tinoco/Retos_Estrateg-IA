def gcd(a, b):
    # Calcula el máximo común divisor (MCD) usando el algoritmo de Euclide, debo de asignar %
    while b:
        a, b = b, a % b
    return a

def solution(n):
    # Inicializa el contador
    count = 0
    
    # Itera sobre 1 hasta n
    for i in range(1, n + 1):
        # Verifica si ""i"" es coprimo con n
        if gcd(n, i) == 1:
            count += 1  # Incrementa el contador si la condicón anterior es correcta
    
    return count

# Casos de prueba
if __name__ == "__main__":
    # Caso 1
    n1 = 5
    resultado1 = solution(n1)
    print(f"Caso 1: {resultado1}")  # Salida esperada: 4

    # Caso 2
    n2 = 49
    resultado2 = solution(n2)
    print(f"Caso 2: {resultado2}")  # Salida esperada: 42

    # Caso 3
    n3 = 1
    resultado3 = solution(n3)
    print(f"Caso 3: {resultado3}")  # Salida esperada: 1

    # Caso 4
    n4 = 69
    resultado4 = solution(n4)
    print(f"Caso 4: {resultado4}")  # Salida esperada: 44

    # Caso 5
    n5 = 10
    resultado5 = solution(n5)
    print(f"Caso 5: {resultado5}")  # Salida esperada: 4, 

    # Caso 6
    n6 = 1
    resultado6 = solution(n6)
    print(f"Caso 3: {resultado6}")  # Salida esperada: 1

# Resultados esperados: yep