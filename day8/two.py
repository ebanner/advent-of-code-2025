import heapq
import math
import sys


def get_junction_boxes():
    lines = [line.strip() for line in sys.stdin]

    junction_boxes = [line.split(',') for line in lines]
    junction_boxes = [tuple(map(int, junction_box)) for junction_box in junction_boxes]

    return junction_boxes


def get_distance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance


def get_distance_matrix(junction_boxes):
    n = len(junction_boxes)

    D = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = get_distance(*junction_boxes[i], *junction_boxes[j])

    return D


def make_graph(junction_boxes):
    G = {}
    return G


def add(G, j1, j2):
    if j1 not in G:
        G[j1] = []

    G[j1].append(j2)


def get_circuit_sizes(G):
    visited = set()

    def bfs(junction_box):
        if junction_box not in visited:
            frontier = {junction_box}
        else:
            frontier = set()

        while True:
            if not frontier:
                break

            new_frontier = set()

            for junction_box in frontier:
                visited.add(junction_box)

                neighbors = G[junction_box]
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue

                    new_frontier.add(neighbor)

            frontier = new_frontier

    circuit_sizes = []
    for junction_box in G:
        num_visited = len(visited)
        bfs(junction_box)
        circuit_size = len(visited) - num_visited
        if circuit_size > 0:
            circuit_sizes.append(circuit_size)

    return circuit_sizes


def get_x_coordinates(j1, j2):
    (x1, _, _), (x2, _, _) = j1, j2
    return x1, x2


if __name__ == '__main__':
    junction_boxes = get_junction_boxes()

    D = get_distance_matrix(junction_boxes)

    n = len(D)
    heap = []
    for i in range(n):
        for j in range(i+1, n):
            heapq.heappush(heap, (D[i][j], (junction_boxes[i], junction_boxes[j])))

    G = make_graph(junction_boxes)
    while True:
        (distance, (j1, j2)) = heapq.heappop(heap)
        add(G, j1, j2)
        add(G, j2, j1)

        circuit_sizes = get_circuit_sizes(G)
        if len(circuit_sizes) == 1:
            circuit_size, = circuit_sizes
            if circuit_size == n:
                break

    x1, x2 = get_x_coordinates(j1, j2)

    print(math.prod([x1, x2]))

