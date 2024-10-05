from Graph import Graph
import pandas as pd
def Sig_states(G:Graph):
    #Find the nodes that have transitions different from &
    states=[]
    for node in G.nodes:
        for ad in node.adj:
            if ad[1] !='&':
                states.append(node.tag)
    states.append(G.nodes[-1].tag)
    return sorted(set(states))

def AFD(T, G: Graph, df):
    states = Sig_states(G)
    N = []  # Lista para almacenar los registros de estados simétricos
    for i in range(len(T)):
        symbol, numbers = T[i]
        T[i] = (symbol, [num for num in numbers if num in states])
    Tres = list(T)
    dic = {}
    
    for lett, numbs in T:
        for other_lett, other_numbs in T:
            if lett != other_lett and numbs == other_numbs:
                # Determinar cuál es el estado lexicográficamente menor
                state_to_keep = min(lett, other_lett)
                state_to_remove = max(lett, other_lett)
                
                if state_to_keep in dic:
                    dic[state_to_keep].append(state_to_remove)
                else:
                    dic[state_to_keep] = [state_to_remove]
                
                # Agregar a la lista N el mensaje de simetría antes de eliminar
                N.append(f'{state_to_keep} is identical to {state_to_remove}')
                
                T.remove((other_lett, other_numbs))
                df = df[df['states'] != state_to_remove]
    
    # Reemplazar los estados eliminados en el dataframe
    for key, values in dic.items():
        for col in df.columns:
            if col != 'state':
                for value in values:
                    df.loc[df[col] == value, col] = key
    
    return df, Tres, N  # Devolver también la lista N

