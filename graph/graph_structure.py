from collections import defaultdict
from typing import Any


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, p1: Any, p2: Any) -> None:
        """Adds edge point1 (p1) - point2 (p2) to the graph."""
        self.graph[p1].append(p2)
        # self.graph[p2].append(p1)
