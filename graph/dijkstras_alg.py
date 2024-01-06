def dijkstra(graph: dict, start_vertex: int) -> dict:
    """Dijkstra's algorithm is a method of finding the shortest paths
    from one vertex of a graph to all the others.
    At each step, the algorithm chooses the least distant vertex and
    moves to it, then to the next vertex, and so on until it reaches
    the goal.
    The key point is this: if optimal decisions are made at each step,
    the final solution is likely to be optimal as well. Algorithms
    that work according to this principle are called greedy.

    Complexity: O(N^2) (but with min-priority queue it drops down to O(N + elog N)).

    Example:
        1) Init graph, distances and visited dict
        g = {
            'A': {'B': 7, 'E': 4},
            'B': {'A': 7, 'C': 5, 'F': 2},
            'C': {'B': 5, 'D': 11, 'F': 6},
            'D': {'C': 11, 'E': 8, 'F': 9},
            'E': {'A': 4, 'D': 8, 'F': 3},
            'F': {'B': 2, 'C': 6, 'D': 9, 'E': 3}
        }
        distances = {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
        visited = {'A': false, 'B': false, 'C': false, 'D': false, 'E': false, 'F': false}

        2) Choose 'A' as the starting point and find distances to the connected vertices
        distances['B'] = min(inf, 0 + 7)
        distances['E'] = min(inf, 0 + 4)
        distances = {'A': 0, 'B': 7, 'C': inf, 'D': inf, 'E': 4, 'F': inf}
        visited = {'A': true, 'B': false, 'C': false, 'D': false, 'E': false, 'F': false}

        3) 'E' is the nearest not visited vertex
        distances['A'] = min(0, 4 + 4)
        distances['D'] = min(inf, 4 + 8)
        distances['F'] = min(inf, 4 + 3)
        distances = {'A': 0, 'B': 7, 'C': inf, 'D': 12, 'E': 4, 'F': 7}
        visited = {'A': true, 'B': false, 'C': false, 'D': false, 'E': true, 'F': false}

        4) 'B' is the nearest not visited vertex
        distances['A'] = min(0, 7 + 7)
        distances['C'] = min(inf, 7 + 5)
        distances['F'] = min(7, 7 + 2)
        distances = {'A': 0, 'B': 7, 'C': 12, 'D': 12, 'E': 4, 'F': 7}
        visited = {'A': true, 'B': true, 'C': false, 'D': false, 'E': true, 'F': false}

        5) 'F' is the nearest not visited vertex
        distances['B'] = min(7, 7 + 2)
        distances['C'] = min(12, 7 + 6)
        distances['D'] = min(12, 7 + 9)
        distances['E'] = min(4, 7 + 3)
        distances = {'A': 0, 'B': 7, 'C': 12, 'D': 12, 'E': 4, 'F': 7}
        visited = {'A': true, 'B': true, 'C': false, 'D': false, 'E': true, 'F': true}

        6) 'C' is the nearest not visited vertex
        distances['B'] = min(7, 12 + 6)
        distances['D'] = min(12, 12 + 11)
        distances['F'] = min(7, 12 + 6)
        distances = {'A': 0, 'B': 7, 'C': 12, 'D': 12, 'E': 4, 'F': 7}
        visited = {'A': true, 'B': true, 'C': true, 'D': false, 'E': true, 'F': true}

        7) 'D' is the nearest not visited vertex
        distances['C'] = min(12, 12 + 11)
        distances['E'] = min(4, 12 + 8)
        distances['F'] = min(7, 12 + 9)
        distances = {'A': 0, 'B': 7, 'C': 12, 'D': 12, 'E': 4, 'F': 7}
        visited = {'A': true, 'B': true, 'C': true, 'D': true, 'E': true, 'F': true}

        8) all vertices visited, and we've got the end results
        distances = {'A': 0, 'B': 7, 'C': 12, 'D': 12, 'E': 4, 'F': 7}
    """
    distances = {vert: float("inf") for vert in graph.keys()}
    visited = {k: False for k in graph.keys()}

    v = list(graph.keys())[start_vertex]
    visited[v] = True
    distances[v] = 0
    for v, d in graph[v].items():
        distances[v] = d

    while not all(visited.values()):
        # find not visited vertex with min distance from start
        min_v, min_d = None, float("inf")
        for v, b in visited.items():
            if not b and distances[v] < min_d:
                min_d = distances[v]
                min_v = v

        visited[min_v] = True
        for v, d in graph[min_v].items():
            distances[v] = min(distances[v], distances[min_v] + d)
    return distances


if __name__ == '__main__':
    g = {
        'A': {'B': 4, 'C': 7},
        'B': {'A': 4, 'D': 2, 'E': 8},
        'C': {'A': 7, 'D': 2, 'E': 5},
        'D': {'B': 2, 'C': 2, 'E': 1, 'F': 4},
        'E': {'C': 5, 'D': 1, 'F': 11},
        'F': {'B': 8, 'D': 4, 'E': 11}
    }
    print(dijkstra(g, 0))
