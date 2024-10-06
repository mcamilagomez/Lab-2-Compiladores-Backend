import json
def graph_to_dict(graph):
    #Transform a graph to a dictionary
    graph_dict = {
        'nodes': []
    }
    for node in graph.nodes:
        node_dict = {
            'tag': node.tag,
            'initial': node.initial,
            'final': node.final,
            'adj': [(n.tag, s) for n, s in node.adj]  # make a list node.tag, chart 
        }
        graph_dict['nodes'].append(node_dict)
    
    return graph_dict
def generate_json(boolean_value, alphabet, graph, Transition_table, AFDnop, T, AFDop, states, identical):
    if boolean_value:
        result = {
            'alphabet': alphabet,
            'graph': graph_to_dict(graph),
            'Transition_table': Transition_table.to_dict(),  # Df to dict
            'AFDnop': AFDnop.to_dict(),  #Df to dict
            'T': [(t[0], t[1]) for t in T],  # Serialize the list of tuples
            'AFDop': AFDop.to_dict(),  # Df to dict
            'states': [(s[0], s[1]) for s in states],  # Serialize the list of tuples
            'identical': identical
        }
    return json.dumps(result, indent=4)  # empty JSON

def generate_emptyjson2(boolean_value):
    result = {}  # empty JSON
    return json.dumps(result, indent=4)  # empty JSON