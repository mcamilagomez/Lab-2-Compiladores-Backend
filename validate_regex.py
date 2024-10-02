import re

def is_simple_regex(expression: str) -> bool:
    # Define the pattern that restricts the allowed operators and parentheses
    # Allow any symbol, but validate the rules for using operators
    operators = r'\?\+\*\|'
    pattern = r'^[^' + operators + r'].*[^|]$'
    
    # Check if it starts with a valid symbol and does not end with '|'
    if not re.match(pattern, expression):
        return False

    # Validate the balance of parentheses
    balance = 0
    for char in expression:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    
    # If the balance is not 0 at the end, then the parentheses are not properly closed
    if balance != 0:
        return False
    
    # Check that there are no invalid consecutive operators
    for i in range(1, len(expression)):
        if expression[i] in '?+*|':
            # Allow '?' if it's after '*' or '+'
            if expression[i] == '?' and expression[i - 1] in '*+':
                continue
            # No other consecutive operators allowed
            if expression[i - 1] in '?+*|':
                return False
    
    return True