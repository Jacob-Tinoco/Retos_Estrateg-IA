import re

def solution(question):
    # Elimina espacios en blanco al principio y al final, y reduce múltiples espacios a uno
    question = re.sub(r'\s+', ' ', question.strip())
    
    # Corrige el espacio alrededor de la puntuación
    question = re.sub(r'\s*,', ',', question)  # Elimina espacio antes de la coma
    question = re.sub(r',\s*', ', ', question)  # Asegura un espacio después de la coma
    
    # Asegura que la pregunta comience con mayúscula
    question = question.capitalize()
    
    # Asegura que la pregunta termine con un solo signo de interrogación
    if not question.endswith('?'):
        question += '?'
    else:
        question = re.sub(r'\?+', '?', question)  # Reemplaza múltiples signos de interrogación por uno
    
    return question

# Casos de prueba
if __name__ == "__main__":
    # Caso 1
    question1 = "esta no es  una pregunta    relevante , ¿verdad"
    resultado1 = solution(question1)
    print(f"Caso 1: {resultado1}")  # Salida esperada: "Esta no es una pregunta relevante,¿verdad?"

    # Caso 2
    question2 = "¿Es esta respuesta   correcta"
    resultado2 = solution(question2)
    print(f"Caso 2: {resultado2}")  # Salida esperada: "¿Es esta respuesta correcta?"

    # Caso 3
    question3 = "   Brasilia No. 92B Col.   San   Pedro Zacatenco C.P.07360 CDMX   Tel. 55 3994 0156   "
    resultado3 = solution(question3)
    print(f"Caso 3: {resultado3}")  # Salida esperada: "Brasilia No. 92B Col. San Pedro Zacatenco C.P. 07360 CDMX Tel. 55 3994 0156?"

    # Caso 4
    question3 = " ¿lo hago bien don   cangrejo  "
    resultado3 = solution(question3)
    print(f"Caso 3: {resultado3}")  # Salida esperada: "¿lo hago bien don cangrejo?"

# Resultados esperados: yep, 4/4
# jaja 
