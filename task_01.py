import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Graph of some roads Ukraine
G = nx.Graph()
G.add_nodes_from(['Kyiv', 'Kharkiv', 'Odessa', 'Dnipro', 'Donetsk'])
G.add_edges_from([('Kyiv', 'Kharkiv'), ('Kyiv', 'Odessa'), ('Kyiv', 'Dnipro'), ('Kyiv', 'Donetsk'), ('Kharkiv', 'Odessa'), ('Kharkiv', 'Dnipro'), ('Odessa', 'Dnipro'),         ('Dnipro', 'Donetsk'), ('Donetsk', 'Kharkiv')])

G['Kyiv']['Kharkiv']['weight'] = 469
G['Kyiv']['Odessa']['weight'] = 475
G['Kyiv']['Dnipro']['weight'] = 487
G['Kyiv']['Donetsk']['weight'] = 688
G['Kharkiv']['Odessa']['weight'] = 716
G['Kharkiv']['Dnipro']['weight'] = 217
G['Odessa']['Dnipro']['weight'] = 452
G['Dnipro']['Donetsk']['weight'] = 248
G['Donetsk']['Kharkiv']['weight'] = 304

# Print the number of nodes and edges in the graph
print(f'Number of nodes: {G.number_of_nodes()}, number of edges: {G.number_of_edges()}')

# Print degree centrality, closeness centrality, and betweenness centrality
print(f'Degree Centrality: {nx.degree_centrality(G)}')
print(f'Closeness Centrality: {nx.closeness_centrality(G)}')
print(f'Betweenness Centrality: {nx.betweenness_centrality(G)}')

# Plot the graph with edge labels
plt.figure(figsize=(12, 6))
labels = nx.get_edge_attributes(G, 'weight')
pos = nx.circular_layout(G)

# Set the coordinates of nodes
pos['Odessa'] = (0.6, -0.5)
pos['Donetsk'] = (1.9, -0.1)
pos['Kharkiv'] = (1.7, 0.3)
pos['Dnipro'] = (1.5, -0.1)
pos['Kyiv'] = (0.7, 0.4)

nx.draw(G, pos, with_labels=True, font_size=9,
        node_size=2000, node_color='#FFFF87', font_weight='bold')

# Load and display the SVG map as the background
img = mpimg.imread("./assets/map.png")
plt.imshow(img, extent=[-1, 2.5, -1, 1], alpha=0.5)

nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()


