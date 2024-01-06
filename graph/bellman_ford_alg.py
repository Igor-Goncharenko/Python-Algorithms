def bellman_ford(graph: dict, start_vertex: int) -> dict:
    """Bellman-Ford is a single source shortest path algorithm that
     determines the shortest path between a given source vertex and
     every other vertex in a graph. This algorithm can be used on both
     weighted and unweighted graphs.

    Algorithm Steps:
    -The outer loop traverses from 0 to (n - 1);
    -Loop over all edges, check if the next node distance > current node
     distance + edge weight, in this case update the next node distance to
     "current node distance + edge weight".

    Complexity: up to O(N^3).

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

        2) 'A' is start vertex
        distances = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}

        3) 1st iter
        First, go through 'A' ('A' not inf):
            distances['B'] = min(inf, 0 + 7) = 7
            distances['E'] = min(inf, 0 + 4) = 4
        Then, go through 'B' ('B' not inf):
            distances['A'] = min(0, 7 + 7) = 0
            distances['C'] = min(inf, 7 + 5) = 12
            distances['F'] = min(inf, 7 + 2) = 9
        Go through 'C' ('C' not inf):
            distances['B'] = min(12, 12 + 5) = 12
            distances['D'] = min(inf, 12 + 11) = 23
            distances['F'] = min(9, 12 + 6) = 9
        Go through 'D' ('D' not inf):
            distances['C'] = min(12, 23 + 11) = 12
            distances['E'] = min(4, 23 + 8) = 4
            distances['F'] = min(9, 23 + 9) = 9
        Go through 'E' ('E' not inf):
            distances['A'] = min(0, 4 + 4) = 0
            distances['D'] = min(23, 4 + 8) = 12
            distances['F'] = min(9, 4 + 3) = 7
        And go through 'F' ('F' not inf):
            distances['B'] = min(12, 7 + 2) = 9
            distances['C'] = min(12, 7 + 6) = 12
            distances['D'] = min(12, 7 + 9) = 12
            distances['E'] = min(4, 7 + 3) = 4
        distances = {'A': 0, 'B': 9, 'C': 12, 'D': 12, 'E': 4, 'F': 7}

        3) 4 more iterations and minimum distances will be found
        distances = {'A': 0, 'B': 7, 'C': 12, 'D': 12, 'E': 4, 'F': 7}
     """
    distances = {vert: float("inf") for vert in graph.keys()}

    v = list(graph.keys())[start_vertex]
    distances[v] = 0

    for _ in range(len(graph) - 1):
        for u, edges in graph.items():
            for v, w in edges.items():
                distances[v] = min(distances[v], distances[u] + w)

    for u, edges in graph.items():
        for v, w in edges.items():
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                raise ValueError("Graph contains negative weight cycle.")

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
    print(bellman_ford(g, 0))
