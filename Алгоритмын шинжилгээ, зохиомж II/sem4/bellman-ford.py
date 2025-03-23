def bellman_ford(graph, source):
    distance = {vertex: float("inf") for vertex in graph}
    predecessor = {vertex: None for vertex in graph}
    distance[source] = 0

    
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

    return distance, predecessor


def reconstruct_path(predecessor, source, end_vertex):
    path = []
    current = end_vertex
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    return path if path[0] == source else None


def find_shortest_paths_to_target(graph, end_vertex):
    results = {}

    for source in graph:
        distances, predecessors = bellman_ford(graph, source)

        if distances[end_vertex] != float("inf"):
            path = reconstruct_path(predecessors, source, end_vertex)
            results[source] = {
                "distance": distances[end_vertex],
                "path": path
            }
    
    return results



graph = {
    "0": {"6": -3, "4": 5, "7": 10},
    "1": {"2": 5, "4": 8, "0": 9},
    "2": {"3": -2, "4": 4},
    "3": {"7": 17},
    "4": {"5": 7, "6": -1},
    "5": {"7": 11, "3": -5},
    "6": {"5": -6, "7": 13},
    "7": {},
}


end_vertex = "5"


shortest_paths = find_shortest_paths_to_target(graph, end_vertex)


for source, data in shortest_paths.items():
    print(f"Source: {source} -> {end_vertex}")
    print(f"Shortest Distance: {data['distance']}")
    print(f"Path: {' -> '.join(data['path'])}\n")
