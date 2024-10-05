def find_matching_parenthesis(subregex: str) -> tuple:
    # Initialize the balance to 1 since we know the first character is '('
    balance = 1
    length = 1  # We already count the first '('

    # Iterate through the string starting from the second character (index 1)
    for i in range(1, len(subregex)):
        char = subregex[i]
        length += 1

        if char == '(':
            balance += 1  # Increase balance if another '(' is found
        elif char == ')':
            balance -= 1  # Decrease balance when a ')' is found
        
        # When balance reaches 0, we've found the matching closing parenthesis
        if balance == 0:
            # Return the content between the first '(' and its matching ')', along with the length
            return subregex[1:i], length
    
    # If no matching closing parenthesis is found, return '' and 0
    return '', 0


def is_simple_regex(regex: str) -> bool:
    no_in = ['*','+','?',')','|']
    no_end = ['(','|']
    no_next_alt=['|','+','*','?',')']
    #'' is not a r.e.
    if regex == '':
        return False
    #Don't start with *,+,?,),|
    if regex[0] in no_in:
        return False
    #Don't finish with (, |
    if regex[-1] in no_end:
        return False
    i=0
    while i<len(regex):
        chart = regex[i]
        #Find the next chart except for the last one
        if i<len(regex)-1:
            next=regex[i+1]
        else:
            next=''
        if chart=='(':
            #Find the r.e. inside (), When there is maldistribution of the parentheses return '', 0
            subregex, mov = find_matching_parenthesis(regex[i:])
            if subregex=='':
                return False
            #The r.e. inside () should be valid
            if not is_simple_regex(subregex):
                return False
            # Move to the )
            i = i+mov-1
        if chart == '*' or chart == '+':
            #Two operatos error 
            if next == '*' or next == '+':
                return False
            #Should be a valid r.e. before + or *
            if not(is_simple_regex(regex[:i])):
                return False
        if chart=='?':
            # Two ??
            if next == '?':
                return False
            #Should be a valid r.e. before ?
            if not (is_simple_regex(regex[:i])):
                return False
        if chart == '|':
            #Next chart do not be |, ), + *
            if next in no_next_alt:
                return False
            #Should be a valid r.e. before and after |
            if not(is_simple_regex(regex[:i]) and is_simple_regex(regex[i+1:])):
                return False
            #Move to the end of the expression
            i = len(regex)-1
        #No balanced parentheses
        if chart==')':
            return False
        i+=1
    return True

