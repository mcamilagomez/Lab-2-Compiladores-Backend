import re

def is_simple_regex(expression: str) -> bool:
    # Define the allowed operators
    operators = r'\?\+\*\|'
    
    # Check if the expression follows a basic format
    # It should not end with an operator, especially '|'
    pattern = r'^[^' + operators + r'].*[^|]$'
    
    # Validate if the expression starts or ends incorrectly
    if not re.match(pattern, expression):
        return False

    # Validate balanced parentheses
    balance = 0
    inside_parenthesis = False  # To track if we are inside parentheses
    content_between_parentheses = False  # To check if there's content inside parentheses

    for i, char in enumerate(expression):
        if char == '(':
            balance += 1
            inside_parenthesis = True
            content_between_parentheses = False  # Reset check for new parentheses
        elif char == ')':
            balance -= 1
            if balance < 0:  # Closing parenthesis without an opening one
                return False
            inside_parenthesis = False
            # If a closing parenthesis appears without content between them, it's invalid
            if not content_between_parentheses:
                return False
        elif inside_parenthesis:
            # Detect if there's content between parentheses
            content_between_parentheses = True

        # Check invalid use of the pipe `|`
        if char == '|':
            # Ensure there's valid content on both sides of the pipe
            if i == 0 or i == len(expression) - 1:
                return False  # Pipe can't be at the beginning or end
            if expression[i - 1] in '|()' or expression[i + 1] in '|()':
                return False  # Pipe can't be preceded or followed by '(', ')' or '|'

    if balance != 0:  # Unbalanced parentheses
        return False
    
    # Validate that there are no consecutive invalid operators
    for i in range(1, len(expression)):
        if expression[i] in '?+*|':
            # Allow `?` if it follows `*` or `+`
            if expression[i] == '?' and expression[i - 1] in '*+':
                continue
            # Allow `|` after `*` or `+`, but make sure it doesn't end with '|'
            if expression[i] == '|' and expression[i - 1] not in '|':
                continue
            # Do not allow other consecutive operators
            if expression[i - 1] in '?+*|':
                return False

    return True

