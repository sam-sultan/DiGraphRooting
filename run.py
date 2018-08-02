import networkx as nx
import matplotlib.pyplot as plt

"""
A function that changes the root node in a rooted directed graph tree.
@param graph: the graph tree
@param node: the node index to be the new root node
* Notes: the tree must have n nodes with (n-1) edges
"""
def rootGraph(G, node):

    # Convert the directed graph to undirected
    G = G.to_undirected()

    # New Directed graph
    H = nx.DiGraph()
    for n in G.nodes:
        H.add_node(n)
        if 'x' in H.nodes[n].keys():
            H.nodes[n]['x'] = G.nodes[n]['x']
        if 'y' in H.nodes[n].keys():
            H.nodes[n]['y'] = G.nodes[n]['y']
        if 'z' in H.nodes[n].keys():
            H.nodes[n]['z'] = G.nodes[n]['z']
        if 'radius' in H.nodes[n].keys():
            H.nodes[n]['radius'] = G.nodes[n]['radius']

    # get the terminal nodes
    terminals = []
    # get list of terminal nodes
    for n in G.nodes:
        if len(list(G.neighbors(n))) == 1:
            terminals.append(n)

    # loop through the terminals and compute shortest path to the new node
    # recreate a new directed graph
    for t in terminals:
        # shortest path as a list of nodes
        path = nx.shortest_path(G, source=t, target=node)
        i = 0
        while i < len(path) - 1:
            H.add_edge(path[i], path[i + 1])
            i += 1

    # return the new directed graph
    return H

# Create a digraph
G = nx.DiGraph()

# add nodes
for i in range(1, 7):
    G.add_node(i)

# add edges
G.add_edge(2, 1)
G.add_edge(3, 2)
G.add_edge(4, 2)
G.add_edge(5, 3)
G.add_edge(6, 3)

# root the graph
G = rootGraph(G, 3)

nx.draw_circular(G, with_labels=True)
plt.show()
