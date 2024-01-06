def find(parent, i):
    """"""
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    """"""
    if rank[x] < rank[y]:
        parent[x] = y

    elif rank[x] > rank[y]:
        parent[y] = x

    else:
        parent[y] = x
        rank[x] += 1


def kruskal_mst(graph: dict) -> list:
    """Kruskal's Minimum Spanning Tree (MST) Algorithm.

    """
    edges = []
    for u, eds in graph.items():
        for v, w in eds.items():
            if (u, v, w) not in edges and (v, u, w) not in edges:
                edges.append((u, v, w))
    edges = sorted(edges, key=lambda x: x[2])

    result = []
    parent = []
    rank = []

    for i in range(len(graph)):
        parent.append(i)
        rank.append(0)

    while len(result) < len(graph) - 1:
        # pick the smallest edge
        u, v, w = edges.pop(0)

        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append([u, v, w])
            union(parent, rank, x, y)

    return result


if __name__ == '__main__':
    g = {
        0: {1: 10, 2: 6, 3: 5},
        1: {0: 10, 3: 15},
        2: {0: 6, 3: 4},
        3: {0: 5, 1: 15, 2: 4}
    }
    print(kruskal_mst(g))
