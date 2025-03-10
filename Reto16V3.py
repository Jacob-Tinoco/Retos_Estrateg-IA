def solution(n, m):
    # Calcula la cantidad de celdas pintadas de negro
    return n + m - 1

# Casos de prueba
if __name__ == "__main__":
    # Prueba 1
    resultado1 = solution(3, 4)
    print(f"Para n=3 y m=4, la salida es: {resultado1}")  # Salida esperada: 6

    # Prueba 2
    resultado2 = solution(3, 3)
    print(f"Para n=3 y m=3, la salida es: {resultado2}")  # Salida esperada: 7

    # Otras pruebas
    resultado3 = solution(2, 5)
    print(f"Para n=2 y m=5, la salida es: {resultado3}")  # Salida esperada: 6

    resultado4 = solution(1, 1)
    print(f"Para n=1 y m=1, la salida es: {resultado4}")  # Salida esperada: 1

    resultado5 = solution(10, 10)
    print(f"Para n=10 y m=10, la salida es: {resultado5}")  # Salida esperada: 19

    resultado6 = solution(33, 44)
    print(f"Para n=10 y m=10, la salida es: {resultado6}")  # Salida esperada: 86


# Resultados esperados:  5/6 
