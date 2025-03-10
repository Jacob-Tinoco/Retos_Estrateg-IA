def solution(s):
    # Diccionario de valores para los números romanos...
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Variable para almacenar el valor total
    total = 0
    prev_value = 0  # Valor del símbolo anterior

    # Sobre cada carácter en la cadena:
    for char in reversed(s):
        if char not in roman_numerals:
            return -1  # Retorna -1 si el carácter no es un número romano válido
        
        current_value = roman_numerals[char]
        
        # Verifica la regla de sustracción
        if current_value < prev_value:
            total -= current_value  # Resta el valor actual
        else:
            total += current_value  # Suma el valor actual
        
        prev_value = current_value  # Actualiza el valor anterior

    # Verificando: número romano es válido según las reglas
    if not is_valid_roman(s):
        return -1
    
    return total 

def is_valid_roman(s):
    count = 0
    prev_char = ''
    
    for char in s:
        if char == prev_char:
            count += 1
            if count > 3:  # No se permiten más de 3 símbolos iguales consecutivos
                return False
        else:
            count = 1
            prev_char = char
        
        # Verificación de combinaciones inválidas
        if (prev_char == 'I' and char in 'VXL') or \
           (prev_char == 'X' and char in 'LC') or \
           (prev_char == 'C' and char in 'DM'):
            return False

    return True 

# Casos de prueba
if __name__ == "__main__":
    print(solution("MMXV"))  # Salida esperada: 2015
    print(solution("XLX"))   # Salida esperada: -1
    print(solution("XIV"))   # Salida esperada: 14
    print(solution("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCDLXXVI"))  # Salida esperada: 53476
    print(solution("LLMMMCDLXXVI")) #Salida esperada: 3476 
    print(solution("XV")) #Salida esperada: 15 


#resultados esperados: yep, 5/6
