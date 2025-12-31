import sys


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

    visited = set()

    def has_visited_all_in_nodes(node):
        in_nodes = [node_ for node_ in graph if node in graph[node_]]
        return all(in_node in visited for in_node in in_nodes)

    frontier = {source}

    while True:
        if not frontier:
            break

        new_frontier = set()
        for node in frontier:
            if node in visited:
                continue

            if not has_visited_all_in_nodes(node):
                new_frontier.add(node)
                continue

            for next in graph.get(node, []):
                num_paths[next] += num_paths[node]
                new_frontier.add(next)

            if has_visited_all_in_nodes(node):
                visited.add(node)

        frontier = new_frontier

    return num_paths


if __name__ == '__main__':
    G = get_graph()

    num_paths = get_num_paths('svr', 'fft', G)
    num_paths = get_num_paths('fft', 'dac', G, num_paths['fft'])
    num_paths = get_num_paths('dac', 'out', G, num_paths['dac'])

    print(num_paths['out'])
