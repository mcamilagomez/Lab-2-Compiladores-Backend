from Thompson_Graph import Graph
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
    # Sort the list
    return sorted(closure)

def move(states:list, G:Graph, symbol:str):
    result=[]
    #For each node in States list find the adjacencies with symbol
    for state in states:
        node = next(n for n in G.nodes if n.tag == state)
        for trans, label in node.adj:
            if label == symbol and trans.tag not in result:
                result.append(trans.tag)
    return sorted(result)

def epsilon_clousureT(T:list, G:Graph):
    result =[]
    #For each state in T find the epsilon clousure of state
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
        
        # Look for the Chart in T that matches the value of 'States'
        for t in T:
            string, int_list = t
            
            if state == string:
                # Check if the value 0 and/or the tag value is in the  list
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
    #Generate a df ['states', 'a1',...,'an']
    col = ['states']+alphabet
    df = pd.DataFrame(columns=col)
    #Find the last node in thompson Graph 
    f = next((nodo for nodo in G.nodes if nodo.final), None)
    # Cerradura-E(0)
    A=epsilon_clousure(0,G)
    # Add to the states list 
    T=Generate_T([],A)
    #Non check states queue
    queue=[T[0]]
    while queue:
        row=[]
        #Check the state
        L=queue.pop(0)
        #Add the label state
        row.append(L[0])
        for element in alphabet:
            # Crerradura-E(mueve(Ax, ax))
            x=epsilon_clousureT(move(L[1],G,element),G)
            if x:
                #If exists find x in states list  
                for symbol, compare in T:
                    if x == compare:
                        label = symbol
                        break
                    else:
                        label = ''
                # If x is not in the states list add to states listk and non check states queue
                if label == '':
                    T=Generate_T(T, x)
                    queue.append(T[-1])
                    label = T[-1][0]
                #Transition
                row.append(label)
            else:
                #if the state doesn't have transition with ax
                row.append('')
        #Add the row in the df
        df.loc[len(df)]=row
    #At the end add the values -> or * in the states that have the initial and final node in thompson graph
    df = assign_values(df, T, f.tag)
    return df, T


