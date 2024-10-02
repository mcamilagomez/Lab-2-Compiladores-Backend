from Thompson_Graph import Graph, printgraph, thompson
from Alphabet_from_regex import Alphabet
import pandas as pd
def epsilon_clousure(node_tag: int, G:Graph) -> list:
    # Find the initial node whose tag matches node_tag
    initial_node = next(n for n in G.nodes if n.tag == node_tag)
    
    # List to store the tags of nodes in the epsilon closure
    closure = [initial_node.tag]
    
    # Queue to process nodes with '&' transitions
    queue = [initial_node]
    
    # While there are nodes in the queue, look for their adjacencies
    while queue:
        node = queue.pop(0)
        
        # Traverse the adjacencies of the current node
        for neighbor, symbol in node.adj:
            if symbol == '&' and neighbor.tag not in closure:
                closure.append(neighbor.tag)
                queue.append(neighbor)
    # Remove duplicates and sort the list
    return sorted(closure)

def move(states:list, G:Graph, symbol:str):
    result=[]
    for state in states:
        node = next(n for n in G.nodes if n.tag == state)
        for trans, label in node.adj:
            if label == symbol and trans.tag not in result:
                result.append(trans.tag)
    return sorted(result)
def epsilon_clousureT(T:list, G:Graph):
    result =[]
    for state in T:
        result.extend(epsilon_clousure(state, G))
    return sorted(set(result))

def Generate_T(T: list, set_values: list) -> list:
    # Check if T is empty
    if not T:
        # If it's empty, generate the first tuple ('A', set_values) and add it to T
        T.append(('A', set_values))
    else:
        # If T is not empty, find the last tuple and get its first value
        last_letter = T[-1][0]
        
        # Get the next uppercase letter
        next_letter = chr(ord(last_letter) + 1)
        
        # Create the new tuple with the next letter and set_values, and add it to T
        T.append((next_letter, set_values))
    
    # Return the modified list T
    return T
def assign_values(df, T, tag):
    # Create an empty 'values' column in the DataFrame
    df['values'] = ''
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        state = row['states']
        
        # Look for the string in T that matches the value of 'States'
        for t in T:
            string, int_list = t
            
            if state == string:
                # Check if the value 0 and/or the tag value is in the integer list
                has_zero = 0 in int_list
                has_tag = tag in int_list
                
                if has_zero and has_tag:
                    df.at[index, 'values'] = '->*'
                elif has_zero:
                    df.at[index, 'values'] = '->'
                elif has_tag:
                    df.at[index, 'values'] = '*'
                break
    
    # Move the 'values' column to be the first column in the DataFrame
    cols = ['values'] + [col for col in df.columns if col != 'values']
    df = df[cols]
    
    return df

def subset_method(G:Graph, alphabet:list):
    col = ['states']+alphabet
    df = pd.DataFrame(columns=col)
    f = next((nodo for nodo in G.nodes if nodo.final), None)
    A=epsilon_clousure(0,G)
    T=Generate_T([],A)
    queue=[T[0]]
    while queue:
        row=[]
        L=queue.pop(0)
        row.append(L[0])
        for element in alphabet:
            x=epsilon_clousureT(move(L[1],G,element),G)
            if x:
                for symbol, compare in T:
                    if x == compare:
                        label = symbol
                        break
                    else:
                        label = ''
                if label == '':
                    T=Generate_T(T, x)
                    queue.append(T[-1])
                    label = T[-1][0]
                row.append(label)
            else:
                row.append('')
            
        df.loc[len(df)]=row
    df = assign_values(df, T, f.tag)
    print(T)
    return df, T

def Sig_states(G:Graph):
    states=[]
    for node in G.nodes:
        for ad in node.adj:
            if ad[1] !='&':
                states.append(node.tag)
    states.append(G.nodes[-1].tag)
    return sorted(set(states))

def AFD(T, states, df):
    for i in range(len(T)):
        symbol , numbers = T[i]
        T[i] = (symbol, [num for num in numbers if num in states])
    dic ={}
    for lett , numbs in T:
        for other_lett, other_numbs in T:
            if lett != other_lett and numbs == other_numbs:
                if lett in dic:
                    dic[lett].append(other_lett)
                else:
                    dic[lett]=[other_lett]
                T.remove((other_lett, other_numbs))
                df = df[df['states'] != other_lett]
    for key, values in dic.items():
        for col in df.columns:
            if col != 'state':
                for value in values:
                    df.loc[df[col] == value, col] = key
    return df

prueba = Graph()
regex = '(a|b)*abb'
alp = Alphabet(regex)
print(f'alfabeto: {alp}')
prueba = thompson(regex)
print('---------------Grafo de Thompson----------------------------------')
printgraph(prueba)
states = Sig_states(prueba)
print('---------------AFD no optimo----------------------------------')
df, T = subset_method(prueba,alp)
print(df)
AFDopt =AFD(T,states, df)
print('---------------AFD Optimo----------------------------------')
print(AFDopt)
