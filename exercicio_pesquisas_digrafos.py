import heapq

# Algoritmo de Dijkstra para encontrar o caminho mais curto de um vértice de origem para todos os outros vértices
def dijkstra(graph, start):
    # Inicializa as distâncias como infinito para todos os vértices exceto o de origem
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # A distância do vértice de origem para ele mesmo é 0
    pq = [(0, start)]  # Uma fila de prioridade para acompanhar os vértices e suas distâncias

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)  # Obtém o vértice com menor distância

        # Se já encontramos um caminho mais curto para este vértice, ignoramos
        if current_distance > distances[current_vertex]:
            continue

        # Itera sobre os vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Se a nova distância for menor do que a atual, atualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Algoritmo de Bellman-Ford para encontrar o caminho mais curto de um vértice de origem para todos os outros vértices
def bellman_ford(graph, start):
    # Inicializa as distâncias como infinito para todos os vértices exceto o de origem
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # A distância do vértice de origem para ele mesmo é 0

    # Relaxamento das arestas para atualizar as distâncias
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    # Verifica se há ciclo de peso negativo
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] + w < distances[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances

# Algoritmo de Floyd-Warshall para encontrar todos os pares de caminhos mais curtos
def floyd_warshall(graph):
    vertices = list(graph.keys())
    num_vertices = len(vertices)
    distances = {v1: {v2: float('infinity') for v2 in vertices} for v1 in vertices}

    # Inicializa as distâncias conhecidas
    for v1 in vertices:
        distances[v1][v1] = 0
        for v2 in graph[v1]:
            distances[v1][v2] = graph[v1][v2]

    # Calcula as distâncias mínimas entre todos os pares
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

# Função para imprimir o grafo de forma mais visual
def print_graph(graph):
    print("Graph:")
    for vertex, edges in graph.items():
        print(f"{vertex} --> {edges}")

# Exemplo de um digrafo
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 1},
    'C': {'B': 1, 'D': 4},
    'D': {}
}

# Imprime o grafo
print_graph(graph)
print()

# Algoritmo de Dijkstra
start_vertex_dijkstra = 'A'
shortest_distances_dijkstra = dijkstra(graph, start_vertex_dijkstra)
print("Dijkstra:")
for vertex, distance in shortest_distances_dijkstra.items():
    print(f"Shortest distance from {start_vertex_dijkstra} to {vertex}: {distance}")
print()

# Algoritmo de Bellman-Ford
start_vertex_bellman = 'A'
shortest_distances_bellman = bellman_ford(graph, start_vertex_bellman)
print("Bellman-Ford:")
for vertex, distance in shortest_distances_bellman.items():
    print(f"Shortest distance from {start_vertex_bellman} to {vertex}: {distance}")
print()

# Algoritmo de Floyd-Warshall
all_shortest_distances_floyd = floyd_warshall(graph)
print("Floyd-Warshall:")
for start_vertex in all_shortest_distances_floyd:
    for end_vertex, distance in all_shortest_distances_floyd[start_vertex].items():
        print(f"Shortest distance from {start_vertex} to {end_vertex}: {distance}")
    print()
