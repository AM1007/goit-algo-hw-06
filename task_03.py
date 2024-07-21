def print_table(distances):
    # Top row of the table
    print("{:<15} {:<15}".format("Vertex", "Distance"))
    print("-" * 25)

    # Output data for each vertex
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        print("{:<15} {:<15}".format(vertex, distance))


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    return distances


graph = {
    'Kyiv': {'Kharkiv': 469, 'Odesa': 475, 'Donetsk': 688, 'Dnipro': 487},
    'Kharkiv': {'Kyiv': 469, 'Odesa': 716, 'Dnipro': 224, 'Donetsk': 304},
    'Odesa': {'Kyiv': 475, 'Kharkiv': 716, 'Dnipro': 452},
    'Donetsk': {'Kyiv': 688, 'Kharkiv': 304, 'Dnipro': 248},
    'Dnipro': {'Kyiv': 487, 'Kharkiv': 217, 'Odesa': 452, 'Donetsk': 248}
}


for city in graph.keys():
    print()
    print(f'Shortest path from vertex {city} to other vertices of the graph')
    print_table(dijkstra(graph, city))