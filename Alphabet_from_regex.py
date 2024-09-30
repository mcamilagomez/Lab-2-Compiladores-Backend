def Alphabet(regex):
    operators = ['+','*','|','?', '(', ')', '&']
    alphabet =[]
    i=0
    while i <len(regex):
        chart = regex[i]
        if chart not in operators:
            if chart not in alphabet:
                alphabet.append(chart)
        i+=1
    return sorted(alphabet)