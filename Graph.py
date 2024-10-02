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
