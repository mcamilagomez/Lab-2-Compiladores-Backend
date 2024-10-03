import re

def is_simple_regex(expression: str) -> bool:
    # Definir los operadores permitidos
    operators = r'\?\+\*\|'
    
    # Comprobar si la expresión cumple con un formato básico
    # No debe terminar con un operador, especialmente '|'
    pattern = r'^[^' + operators + r'].*[^|]$'
    
    # Validar si la expresión no empieza o termina de manera incorrecta
    if not re.match(pattern, expression):
        return False

    # Validar el balance de paréntesis
    balance = 0
    for char in expression:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:  # Paréntesis cerrando sin abrir
                return False
    
    if balance != 0:  # Paréntesis no balanceados
        return False
    
    # Validar que no haya operadores consecutivos inválidos
    for i in range(1, len(expression)):
        if expression[i] in '?+*|':
            # Permitir `?` si va después de `*` o `+`
            if expression[i] == '?' and expression[i - 1] in '*+':
                continue
            # Permitir `|` después de `*` o `+`, pero validar que no termine en '|'
            if expression[i] == '|' and expression[i - 1] not in '|':
                continue
            # No permitir otros operadores consecutivos
            if expression[i - 1] in '?+*|':
                return False

    return True
