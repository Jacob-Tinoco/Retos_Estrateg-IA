def solution(image):
     # Verificar si la imagen está vacía
    if not image: 
        return 0

    rows = len(image)
    cols = len(image[0])
    visited = [[False] * cols for _ in range(rows)]  # Matriz para pixeles 
    object_count = 0  # Contador de objetos,

    def dfs(r, c):
        # Verificación de los límites y si el pixel es parte del objeto y no ha sido visitado
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] == '0' or visited[r][c]:
            return
        visited[r][c] = True 
        dfs(r + 1, c)  # Abajo
        dfs(r - 1, c)  # Arriba
        dfs(r, c + 1)  # Derecha
        dfs(r, c - 1)  # Izquierda

    # Iteración sobre cada pixel de la imagen
    for r in range(rows):
        for c in range(cols):
            if image[r][c] == '1' and not visited[r][c]:  # Si se encuentra un nuevo objeto
                object_count += 1 
                dfs(r, c)  

    return object_count  

if __name__ == "__main__":
    # Caso 1
    image1 = [['0', '1', '1', '0', '1'],
               ['0', '1', '1', '1', '1'],
               ['0', '0', '0', '0', '1'],
               ['1', '0', '0', '1', '1']]
    print(solution(image1))  # Salida esperada: 2

    # Caso 2
    image2 = [['0', '1', '0', '0', '1'],
               ['1', '1', '0', '0', '0'],
               ['0', '0', '1', '0', '1'],
               ['0', '0', '1', '1', '0'],
               ['1', '0', '1', '1', '0']]
    print(solution(image2))  # Salida esperada: 5

    # Caso 3
    image3 = []
    print(solution(image3))  # Salida esperada: 0

    # Caso 4
    image4 = [["0", "1", "0"],
               ["1", "0", "1"],
               ["0", "1", "0"]]
    print(solution(image4))  # Salida esperada: 4


# Resultados esperados: yep, 4/4