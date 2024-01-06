def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def astar(
        grid: list[list[int]], start: tuple[int, int], target: tuple[int, int]
) -> list[tuple[int, int]] | None:
    """A* algorithm (A star).
    Like Dijkstra's algorithm, A* searches for the distance from the
    start point to the end point. But, unlike the latter, it takes into
    account not only the distance from the current point to the initial
    point, but also a heuristic estimation of this distance.

    Consider a square grid having many obstacles, and we are given an
    initial and a target cell. At each step, the algorithm selects a
    node according to the value of 'f' which is equal to the sum of two
    other parameters, 'g' and 'h':
        'g' = the cost of traveling from the starting point to a given
              grid cell, following the path generated to reach that target.
        'h' = the estimated cost of traveling from a given grid cell to
              the final destination. This is often referred to as a heuristic,
              which is nothing more than a kind of reasonable guess.
              (e.g. 'manhattan distance')

    Algorithm:
        1.  Initialize open list and closed list
            put the starting node on the open list (with value 0)

        2.  Initialize 'came from' and 'g_cost' dict to save previous points info

        3.  while the open list is not empty
            a) find the node with the least f on the open list, call it "q"

            b) pop q off the open list

            c) if q is target, generate path from start to end (use 'came from' dict)
               and return it

            d) generate q's 8 new positions

            d) for each new position
                I) if new pos out of field -> continue
                II) if new pos is obstacle -> continue
                III) if new pos is already in closed list -> continue
                IV) if new point is already in open list with lower f value -> continue
                V) else add new point to open list and add path to 'came from' dict

    Complexity: O(N) where N is number of edges in the graph.
    """
    open_list = [(start, 0)]
    closed_list = []

    came_from = {start: None}
    g_cost = {start: 0}

    while open_list:
        # find point with lowest f value in open list
        current_index = 0
        for index, point in enumerate(open_list):
            if point[1] < open_list[current_index][1]:
                current_index = index
        current_point = open_list.pop(current_index)
        closed_list.append(current_point[0])

        # check if goal is reached -> gen path from start to target
        if current_point[0] == target:
            path = []
            point = current_point[0]
            while point is not None:
                path.append(point)
                point = came_from[point]
            return path

        for new_pos_x, new_pos_y in [(0, -1), (0, 1), (-1, 0), (1, 0),
                                     (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x, y = new_pos_x + current_point[0][0], new_pos_y + current_point[0][1]

            # check if position out of field
            if not 0 <= y <= len(grid[0]) - 1 or not 0 <= x <= len(grid) - 1:
                continue
            # check if position is obstacle
            if grid[x][y] != 0:
                continue
            # check if point is already in the closed list
            if (x, y) in closed_list:
                continue

            g = g_cost[current_point[0]] + 1
            g_cost[(x, y)] = g
            h = manhattan_distance((x, y), target)
            f = g + h

            # check if point is already in open list with lower f value
            if any(p[0] == (x, y) and f >= p[1] for p in open_list):
                continue

            open_list.append(((x, y), f))
            came_from[(x, y)] = current_point[0]

    return None  # No path found


if __name__ == '__main__':
    field = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    s = (7, 0)
    e = (0, 0)
    shortest_path = astar(field, s, e)
    print(shortest_path)
    for y, row in enumerate(field):
        for x, v in enumerate(row):
            if (y, x) in shortest_path:
                print("*", end=" ")
            else:
                print(v, end=" ")
        print()
