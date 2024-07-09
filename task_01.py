import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes (e.g., bus stops)
G.add_node("A", pos=(0, 0))
G.add_node("B", pos=(1, 2))
G.add_node("C", pos=(2, 3))
G.add_node("D", pos=(3, 1))

# Add edges (e.g., bus routes)
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")])

# Visualize the graph
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=15, font_color="black", font_weight="bold")
plt.show()

# Analyze graph characteristics
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Node degrees: {dict(G.degree())}")




# DFS Implementation:

def dfs(graph, start, path=[]):
    path = path + [start]
    for node in graph[start]:
        if node not in path:
            path = dfs(graph, node, path)
    return path

path_dfs = dfs(G, "A")
print(f"DFS Path: {path_dfs}")

# BFS Implementation:

from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(set(graph[node]) - set(visited))
    return visited

path_bfs = bfs(G, "A")
print(f"BFS Path: {path_bfs}")

# Implementing Dijkstra's Algorithm

G.add_weighted_edges_from([("A", "B", 1.5), ("A", "C", 2.5), ("B", "C", 1.0), ("C", "D", 2.0)])

def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, weight in destinations.items():
            weight = weight["weight"]
            total_weight = weight_to_current_node + weight
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, total_weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > total_weight:
                    shortest_paths[next_node] = (current_node, total_weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

shortest_paths = dijkstra(G, "A")
print(shortest_paths)


# Visualize Shortest Paths:

