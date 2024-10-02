class Node:
    def __init__(self, tag, initial, final):
        self.tag = tag
        self.initial = initial
        self.final = final
        self.adj = []  #tuple list (Node, label)
    def add_edge(self, node, chart): #Append to adj tuples
        self.adj.append((node, chart))

class Graph:
    def __init__(self):
        self.nodes = [] #list of nodes
    def element(self, chart):
        # ->|0|--a-->||1|| Base case
        node1 = Node(0, True, False)
        node2 = Node(1, False, True)
        node1.add_edge(node2, chart)
        # Add nodes in graph
        self.nodes.append(node1)
        self.nodes.append(node2)

def concat(G1:Graph, G2:Graph):
    #If we don't have a previous graph return the actual graph
    if not G1.nodes:
        return G2.nodes
    
    #Find the final node from G2 and the initial node from G1
    f = next((node for node in G1.nodes if node.final), None)
    i = next((node for node in G2.nodes if node.initial), None)

    # Tag from the las node of G1
    tag_f = f.tag

    # Change all the tags from G2 (except the initial note) change them for f.tag+1 ++
    for node in G2.nodes:
        if node != i: 
            tag_f += 1
            node.tag = tag_f

    # Save the adjacencies of i because we replace it for f
    res = i.adj[:]

    #Add the adjacencies in f
    f.adj.extend(res)

    #Remove the final flag from f
    f.final = False

    #Join the two graphs
    Gres = G1.nodes + G2.nodes

    # if a Node have adj with i replace for f 
    for node in Gres:
        node.adj = [(f if n == i else n, chart) for n, chart in node.adj]

    # Remove i from the graph
    Gres.remove(i)

    return Gres

def interogate(G:Graph):
    #Create 2 nodes
    nodei=Node(0, True, False)
    nodef=Node(1,False, True)

    #Increment all the tags 
    for node in G.nodes:
        node.tag = node.tag+1

    #Find the initial and final node
    i = next((nodo for nodo in G.nodes if nodo.initial), None)
    f = next((nodo for nodo in G.nodes if nodo.final), None)

    #Add the adjacencies 
    nodei.add_edge(i,'&')
    f.adj.append((nodef, '&'))

    #Remove the initial and final flag from the graph
    i.initial=False
    f.final=False

    #Change the tag from the final node 
    nodef.tag= f.tag +1
    
    #Add adjacencies and addicionate the new nodes in the graph
    nodei.add_edge(nodef,'&')
    G.nodes.append(nodei)
    G.nodes.append(nodef)

    return G.nodes

def kleene_closure(G:Graph):
    #Increment all the tags
    for node in G.nodes:
        node.tag = node.tag+1

    #Find the initial and final node    
    i = next((nodo for nodo in G.nodes if nodo.initial), None)
    f = next((nodo for nodo in G.nodes if nodo.final), None)

    #Create 2 nodes and change the flags of the nodes in the graph
    nodei=Node(0,True,False)
    nodef=Node(f.tag+1,False, True)
    i.initial=False
    f.final=False

    #Add all the adjacencies and append the nodes in the graph
    f.add_edge(i,'&')
    nodei.add_edge(i,'&')
    nodei.add_edge(nodef,'&')
    f.add_edge(nodef,'&')
    G.nodes.append(nodei)
    G.nodes.append(nodef)

    return G.nodes

def positive_closure(G:Graph):
    #Increment all the tags
    for node in G.nodes:
        node.tag = node.tag+1

    #Find the initial and final node 
    i = next((nodo for nodo in G.nodes if nodo.initial), None)
    f = next((nodo for nodo in G.nodes if nodo.final), None)

    #Create 2 nodes and change the flags of the nodes in the graph
    nodei=Node(0,True,False)
    nodef=Node(f.tag+1,False, True)
    i.initial=False
    f.final=False
    #Add all the adjacencies and append the nodes in the graph
    f.add_edge(i,'&')
    nodei.add_edge(i,'&')
    f.add_edge(nodef,'&')
    G.nodes.append(nodei)
    G.nodes.append(nodef)

    return G.nodes

def alt(G1:Graph, G2:Graph):
    #Increment all the tags of G1
    for node in G1.nodes:
        node.tag = node.tag+1
    #Find the initial and final node from G1 and G2 and increment the tags from G2 according the last tag from G1
    i1 = next((nodo for nodo in G1.nodes if nodo.initial), None)
    f1 = next((nodo for nodo in G1.nodes if nodo.final), None)
    for node in G2.nodes:
        node.tag = node.tag+1+f1.tag
    i2 = next((nodo for nodo in G2.nodes if nodo.initial), None)
    f2 = next((nodo for nodo in G2.nodes if nodo.final), None)

    #Create 2 nodes and change the flags of the nodes in the graph
    i1.initial=False
    f1.final=False
    i2.initial=False
    f2.final=False
    nodei=Node(0,True,False)
    nodef=Node(f2.tag+1,False, True)

    #Add all the adjacencies, join G1 and G2; and  append the nodes in the graph
    nodei.add_edge(i1,'&')
    nodei.add_edge(i2,'&')
    f1.add_edge(nodef,'&')
    f2.add_edge(nodef,'&')
    Gres = G1.nodes + G2.nodes
    Gres.append(nodei)
    Gres.append(nodef)
    
    return Gres

def find_subregex(string):
    pila = []
    subregex = ""
    i = 0
    
    while i < len(string):
        char = string[i]

        #Start when we find a (
        if char == '(':
            pila.append('(')  #add to the stacks of (
            subregex += char  #add the (
            i += 1
            #Make this while we have ( into the stack, it is in cases like (a|(b|c)) or (((a|b)))
            while pila:
                char = string[i]
                subregex += char
                if char == '(':
                    pila.append('(')
                elif char == ')':
                    pila.pop()
                i += 1
        
            # add into the subregex * or +
            if i < len(string) and string[i] in ['*', '+']:
                subregex += string[i]
                i += 1
        break

    return subregex, len(subregex)

def extract_interior_and_operator(string):
    stack = []
    interior = ""
    i = 0
    operator = None

    # Iterate over the string to find the opening parentheses
    while i < len(string):
        char = string[i]

        # If we find an opening parenthesis, we start extracting the inner content
        if char == '(':
            stack.append('(')
            i += 1
            # Continue until all parentheses are properly closed
            while stack:
                char = string[i]
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    stack.pop()
                if stack:
                    interior += char  # Only add to interior if we are not at the last closing parenthesis
                i += 1

            # After closing the parentheses, check if the next character is '*' or '+'
            if i < len(string) and string[i] in ['*', '+']:
                operator = string[i]
            else:
                operator = ''
            # Exit the loop as we have found the content inside the parentheses
            break

    return interior, operator, len(interior)

def printgraph(resultado:Graph):
    for nodo in resultado.nodes:
        adj_tags = [(adj_nodo.tag, label) for adj_nodo, label in nodo.adj]  # Extraer tag y label de cada tupla
        print(f"Nodo: {nodo.tag}, Initial: {nodo.initial}, Final: {nodo.final}, Adj: {adj_tags}")

def Sort_by_tag(grafo:Graph):
    grafo.nodes = sorted(grafo.nodes, key=lambda nodo: nodo.tag)
    return grafo

def thompson(regex):
    i=0
    #Generate the graph
    graph = Graph()
    while i<len(regex):
        #Chart
        chart= regex[i]
        #Next chart
        next=''
        #Graph made for do the expresions
        graphaux = Graph()
        if i<(len(regex)-1): next = regex[i+1] 
        #Cases from chart: (, a, | Cases for next when chart is a: ?, *, +
        if chart == "(":
            #Find the expresión in (...) and the operator 
            subregex, operador, movi = extract_interior_and_operator(regex[i:])
            #Make the graph for the subexpresion
            graphaux=thompson(subregex)
            if(operador=='*'):
                #Case (...)*
                graphaux.nodes=kleene_closure(graphaux)
                i=i+movi+2
            elif (operador=='+'):
                #Case (...)+
                graphaux.nodes=positive_closure(graphaux)
                i=i+movi+2
            else:
                #Case (...)
                i=i+movi+1   
            #Join
            graph.nodes=concat(graph,graphaux)
        else:
            if next == '?':
                graphaux.element(chart)
                graphaux.nodes = interogate(graphaux)
                graph.nodes = concat(graph,graphaux)
                i+=1
            elif next == '*':
                graphaux.element(chart)
                graphaux.nodes=kleene_closure(graphaux)
                graph.nodes = concat(graph,graphaux)
                i+=1
            elif next == '+':
                graphaux.element(chart)
                graphaux.nodes=positive_closure(graphaux)
                graph.nodes = concat(graph,graphaux)
                i+=1
            elif chart=='|':
                #Find all the expresion after |
                subregex = regex[i+1 :]
                i = len(regex)-1 #The last element
                #Make the graph of subregex
                graphaux = thompson(subregex)
                #Make | 
                graph.nodes = alt(graph, graphaux)
            else:
                graphaux.element(chart)
                graph.nodes=concat(graph, graphaux)
        graph=Sort_by_tag(graph)
        i+=1
    return graph


'''from Alphabet_from_regex import Alphabet
from Transition_table import transition_table
            
regex="(((ab)*)a)+"
alp= Alphabet(regex)
resultado =Graph()
resultado = thompson(regex)
printgraph(resultado)
table = transition_table(resultado,alp)
print(table)
'''
