# Матриця суміжності

# adj_matrix = [
#   [0, 1, 0, 1], # Вершина А
#   [1, 0, 1, 0], # Вершина В
#   [0, 1, 0, 1], # Вершина С
#   [0, 1, 0, 1], # Вершина D
# ]

# is_edge_AB = adj_matrix[0][1]

# Напішіть функцію, яка приймає матрицю суміжності та повертає 1, якщо існує ребро між конкретними вузлами, i -1, якщо такого ребра не існує. Вузли можна задавати індексами.

# def check_edge(matrix, i, j):
#     if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
#         return -1
#     if matrix[i][j] == 1:
#         return 1
#     return -1

# Список суміжності

# adj_list = {
#   'A': ['B', 'D'],
#   'B': ['A', 'C'],
#   'C': ['B', 'D'],
#   'D': ['A', 'C']
# }

# neighbors_A = adj_list['A']

# Список ребер

# reb_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]


# Цикллічий граф

# cyclic_graph = {
#   'A': ['B', 'D'],
#   'B': ['A', 'C'],
#   'C': ['B', 'D'],
#   'D': ['A', 'C']
# }

# ======================================================================

# Рекурсивна реалізація алгоритму DFS

# def dfs_recursive(graph, vertex, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(vertex)
#     print(vertex, end=' ') # Відвідуємо вершину
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited)

# Представлення графа за допомогою списку сумііжності

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E'] 
# }

# def dfs_recursive(graph, 'A')

# ======================================================================


# Ітеративна реалізація алгоритму DFS

# def dfs_iterative(graph, start_vertex):
#     visited = set()
#     # Використовуємо стек для зберігання вершин
#     stack = [start_vertex]
#     while stack:
#         # Вилучаємо вершину зі стеку
#         vertex = stack.pop()
#         if vertex not in visited:
#             print(vertex, end=' ')
#             # Відвідуємо вершину
#             visited.add(vertex)
#             # Додаємо сусідні вершини до стеку
#             stack.extend(reversed(graph[vertex]))

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E'] 
# }

# dfs_iterative(graph, 'A')

# ======================================================================

# Ітеративна реалізація BFS

# from collections import deque

# def bfs_iterative(graph, start):
#     # Ініціалізація порожньої множини для зберігання відвіданих вершин
#     visited = set()
#     # Ініціалізація черги з початковою вершиною
#     queue = deque([start])

#     while queue:  # Поки черга не порожня, продовжуємо обхід
#         # Вилучаємо першу вершину з черги
#         vertex = queue.popleft()
#         # Перевіряємо, чи була вершина відвідана раніше
#         if vertex not in visited:
#             # Якщо не була відвідана, друкуємо її
#             print(vertex, end=" ")
#             # Додаємо вершину до множини відвіданих вершин
#             visited.add(vertex)
#             # Додаємо всіх невідвіданих сусідів вершини до кінця черги
#             # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
#             queue.extend(set(graph[vertex]) - visited)
#     # Повертаємо множину відвіданих вершин після завершення обходу
#     return visited  

# # Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# Запуск алгоритму BFS
# bfs_iterative(graph, 'A')

# ======================================================================

# Рекурсивна реалізація BFS

# from collections import deque

# def bfs_recursive(graph, queue, visited=None):
#     # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
#     if visited is None:
#         visited = set()
#     # Якщо черга порожня, завершуємо рекурсію
#     if not queue:
#         return
#     # Вилучажмо вершину з початку черги
#     vertex = queue.popleft()
#     # Перевіряємо, чи видалили дану вершину:
#     if vertex not in visited:
#         print(vertex, end=" ")
#         # Додаємо вершину до множини відвіданих вершин.
#         visited.add(vertex)
#         # Додаємо невідвіданих сусідів даної вершини в кінець черги
#         queue.extend(set(graph[vertex]) - visited)
#     # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
#     bfs_recursive(graph, queue, visited)

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# # Запуск рекурсивного адгоритму
# bfs_recursive(graph, deque(['A']))


# ======================================================================

# Бібліотека networkX. Неорієнтовний граф

# import networkx as nx

# G = nx.Graph()

# G.add_node('A')
# G.add_nodes_from(['B', 'C', 'D'])

# G.add_edge('A', 'B')
# G.add_edges_from([('A', 'C'), ('B', 'C'), ('B', 'D')])

# print('Nodes:', G.nodes())
# print('Edges:', G.edges())

# # Вузли які з'єднані між конкретним вузлом
# print(list(G.neighbors('A')))

# # Видалення вузла
# # G.remove_node('A')
# # print('Nodes:', G.nodes())

# # G.remove_nodes_from(['B', 'C'])
# # print('Nodes:', G.nodes())

# G.remove_edge('A', 'B')
# print('Edges:', G.edges())

# G.remove_edges_from([('A', 'C'), ('B', 'D')])
# print('Edges:', G.edges())

# ======================================================================

# Бібліотека networkX. Орієнтовний граф

# import networkx as nx

# DG = nx.DiGraph()

# DG.add_edges_from([("A", "B"), ("B", "C")])
# G = nx.Graph(DG)

# G.add_node(1)
# G.add_node("A")
# G.add_node((2, 3))

# G.add_edge(1, "A", weight=2.5, label='connection')

# print("Nodes:" , G.nodes())
# print("Edges:" , G.edges())

# neighbors_of_A = G["A"]

# edge_info = G["A"]["B"]

# print("Neighbors of A:", neighbors_of_A)
# print("Edge info:", edge_info)

# G.graph["name"] = "My Graph"
# G.nodes["A"]["color"] = "blue"

# G["A"]["B"]["weight"] = 5

# print("Graph name:", G.graph["name"])
# print("Node color:", G.nodes["A"]["color"])
# print("Edge weight:", G["A"]["B"]["weight"])

# G["A"]["B"]["weight"] = 5

# G.add_node("A", color="red")
# G.add_edge("A", "B", weight=4)

# ======================================================================

# Аналіз графів

# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.Graph()

# G.add_node("A")
# G.add_nodes_from(["B", "C", "D"])

# G.add_edge("A", "B")
# G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

# num_nodes = G.number_of_nodes()  # 4
# num_edges = G.number_of_edges()  # 4
# is_connected = nx.is_connected(G)  # True

# degree_centrality = nx.degree_centrality(G)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
# closeness_centrality = nx.closeness_centrality(G)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
# betweenness_centrality = nx.betweenness_centrality(G)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}


# import matplotlib.pyplot as plt
# G = nx.complete_graph(3)
# options = {
#     "node_color": "yellow",
#     "edge_color": "lightblue",
#     "node_size": 500,
#     "width": 3,
#     "with_labels": True
# }
# nx.draw(G, **options)
# plt.show()

# ======================================================================

# Алгоритмом Дейкстри

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'A'))
