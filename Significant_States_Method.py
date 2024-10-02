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
                if lett in dic:
                    dic[lett].append(other_lett)
                else:
                    dic[lett] = [other_lett]
                
                # Agregar a la lista N el mensaje de simetría antes de eliminar
                N.append(f'{lett} is identical to {other_lett}')
                
                T.remove((other_lett, other_numbs))
                df = df[df['states'] != other_lett]
    
    for key, values in dic.items():
        for col in df.columns:
            if col != 'state':
                for value in values:
                    df.loc[df[col] == value, col] = key
    
    return df, Tres, N  # Devolver también la lista N
