def solution(precios, notas, x):
    total = 0.0
    
    # itera sobre cada precio y su nota correspondiente
    for i in range(len(precios)):
        texto = notas[i].split(" ", 1) # Separa el porcentaje de la nota
        
        # Verificar si la nota indica que es más alto que en la tienda
        if "mismo" not in texto:
            if "mas alto" in texto:
                val = texto[0].split("%")
                t = precios[i] * float(val[0]) / 100  # Monto adicional
                r = precios[i] * 100 / (100 + float(val[0]))  # Precio original
                t = precios[i] - r  # Diferencia a pagar
                total += t  # Suma al total
            
            # Verificar si la nota indica que es más bajo que en la tienda
            elif "mas bajo" in texto:
                val = texto[0].split("%")
                r = precios[i] * 100 / (100 - float(val[0]))  # Precio original
                t = r - precios[i]  # Diferencia a pagar
                total -= t  # Resta del total

    return total <= x

# Casos de prueba
# Devuelve True si el total es menor o igual a x, de lo contrario False
if __name__ == "__main__":
    # Caso 1
    precios1 = [110, 95, 70]
    notas1 = ["10.0% mas alto que en la tienda", "5.0% mas bajo que en la tienda", "Lo mismo que en la tienda"]
    x1 = 5
    resultado1 = solution(precios1, notas1, x1)
    print(f"Caso 1: {resultado1}")  # Salida esperada: True

    # Caso 2
    precios2 = [48, 165]
    notas2 = ["20.00% mas alto", "10.00% mas bajo"]
    x2 = 2
    resultado2 = solution(precios2, notas2, x2)
    print(f"Caso 2: {resultado2}")  # Salida esperada: True

    # Caso 3
    precios3 = [24.42, 24.42, 24.2424, 85.23]
    notas3 = ["13.157% mas alto", "13.157% mas bajo", "Lo mismo que en tienda", "19.24% mas alto"]
    x3 = 0
    resultado3 = solution(precios3, notas3, x3)
    print(f"Caso 3: {resultado3}")  # Salida esperada: False
# Resultados esperados: yep