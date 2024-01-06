from typing import Generator
from graph_structure import Graph


def breadth_first_search(graph: Graph, root_vertex: int) -> Generator:
    """Breadth first search.
    Breadth first search is a graph traversal algorithm that starts at the root
    node and explores all of the neighbor nodes at the present depth prior to
    moving on to the nodes at the next depth level.
    Uses Queue data structure.
    Unlike a tree, we have to memorize the visited vertices.
    """
    visited = {k: False for k in graph.graph.keys()}

    v = list(graph.graph.keys())[root_vertex]
    yield v
    visited[v] = True
    queue = graph.graph[v].copy()

    while queue:
        v = queue.pop(0)
        if not visited[v]:
            yield v
            visited[v] = True
            queue.extend(graph.graph[v])


def depth_first_search(graph: Graph, root_vertex: int) -> Generator:
    """Depth first search.
    Depth first search is a graph traversal algorithm that starts at a root node
    and explores as far as possible along each branch before backtracking.
    Uses stack data structure.
    Unlike a tree, we have to memorize the visited vertices.
    """
    visited = {k: False for k in graph.graph.keys()}

    v = list(graph.graph.keys())[root_vertex]
    yield v
    visited[v] = True
    stack = graph.graph[v][::-1].copy()

    while stack:
        v = stack.pop(-1)
        if not visited[v]:
            yield v
            visited[v] = True
            stack.extend(graph.graph[v][::-1])


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(f"Breadth first search: {list(breadth_first_search(g, 2))}")

    print(f"Breadth first search: {list(depth_first_search(g, 2))}")
