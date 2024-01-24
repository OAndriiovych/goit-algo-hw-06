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
    'Alice': {'Bob': 1, 'Charlie': 3, 'Frank': 9},
    'Bob': {'Alice': 1, 'Charlie': 3, 'David': 2},
    'Charlie': {'Alice': 3, 'Bob': 3, 'David': 2},
    'David': {'Bob': 2, 'Charlie': 2, 'Eva': 4},
    'Eva': {'David': 4},
    'Frank': {'Alice': 9, 'Grace': 9},
    'Grace': {'Frank': 9, 'Hank': 9},
    'Hank': {'Grace': 9, 'Ian': 8},
    'Ian': {'Hank': 8, 'Karen': 8},
    'Karen': {'Ian': 8}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'Frank'))
