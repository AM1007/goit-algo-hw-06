import networkx as nx
from collections import deque


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return

    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


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

# Algorithm BFS (recursive)
print('Breadth-first search (BFS):')
bfs_recursive(G, deque(['Kyiv']))
print()
# Algorithm DFS (recursive)
print('Depth-first search (DFS):')
dfs_recursive(G, 'Kyiv')