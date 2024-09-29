import pandas as pd
from Thompson_Graph import Graph

def transition_table(G: Graph, alphabet: list):
    # Inicializamos un diccionario para almacenar las filas
    data = {}
    
    # Iteramos sobre los nodos del grafo
    for node in G.nodes:
        row = []
        for element in alphabet:
            adjacencies = []
            # Verificamos las adyacencias para el nodo y el elemento del alfabeto
            for adj in node.adj:
                if adj[1] == element:
                    adjacencies.append(adj[0].tag)
            row.append(adjacencies)
        # Añadimos las filas al diccionario con la clave como el tag del nodo
        data[node.tag] = row
    
    # Creamos el DataFrame usando el diccionario y el alfabeto como columnas
    df = pd.DataFrame(data, index=alphabet).T
    
    return df
