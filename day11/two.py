import sys

import time


def parse(line):
    node, neighbors_str = line.split(':')

    neighbors = neighbors_str.split()

    return node, neighbors


def get_graph():
    lines = [line.strip() for line in sys.stdin]

    graph = {}
    for line in lines:
        node, neighbors = parse(line)
        graph[node] = neighbors

    return graph



def get_num_paths(source, target, graph, num_paths_init=1):
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs(source)

    def intersect(graph, visited):
        intersected_graph = {}
        for node in graph:
            if node not in visited:
                continue
            intersected_graph[node] = [neighbor for neighbor in graph[node] if neighbor in visited]
        return intersected_graph

    graph = intersect(graph, visited)

    def get_nodes():
        nodes = set()
        for node in graph:
            for node_ in graph[node]:
                nodes.add(node_)
            nodes.add(node)
        return nodes

    num_paths = {node: 0 for node in get_nodes()}
    num_paths[source] = num_paths_init

    def ready(node):
        if node == source:
            return True
        for node_ in graph:
            if node not in graph[node_]:
                continue
            if num_paths[node_] == 0:
                return False
        return True

    frontier = {source}
    while True:
        # print(len(frontier))
        if len(frontier) == 0:
            # print('breaking')
            break

        new_frontier = set()
        for node in frontier:
            if not ready(node):
                new_frontier.add(node)
                continue

            for next in graph.get(node, []):
                num_paths[next] += num_paths[node]
                new_frontier.add(next)

        if frontier == new_frontier:
            break

        frontier = new_frontier

        # print(frontier)

        # print(frontier)

        # time.sleep(.1)

    return num_paths


if __name__ == '__main__':
    G = get_graph()

    num_paths = get_num_paths('svr', 'dac', G)

    print('svr -> dac', num_paths['dac'])

    num_paths = get_num_paths('dac', 'fft', G, num_paths['dac'])

    print('dac -> fft', num_paths.get('fft', 0))

    num_paths = get_num_paths('fft', 'out', G, num_paths.get('fft', 0))

    print('fft -> out', num_paths['out'])

    print()

    svr_dac_fft_out = num_paths['out']

    print('svr -> dac -> fft -> out', svr_dac_fft_out)

    print()

    num_paths = get_num_paths('svr', 'fft', G)

    print('svr -> fft', num_paths['fft'])

    num_paths = get_num_paths('fft', 'dac', G, num_paths['fft'])

    print('fft -> dac', num_paths.get('dac', 0))

    num_paths = get_num_paths('dac', 'out', G, num_paths['dac'])

    print('dac -> out', num_paths['out'])

    print()

    print('svr -> fft -> dac -> out', num_paths['out'])

    print()

    svr_fft_dac_out = num_paths['out']

    print(svr_dac_fft_out + svr_fft_dac_out)
