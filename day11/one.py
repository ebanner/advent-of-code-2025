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


def get_num_paths(graph):
    visited = set()

    def dfs(node, indent=0):
        if node == 'out':
            return 1

        visited.add(node)

        num_paths = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                num_paths += dfs(neighbor, indent+1)

        visited.remove(node)

        return num_paths

    num_paths = dfs('you')

    return num_paths


if __name__ == '__main__':
    graph = get_graph()

    num_paths = get_num_paths(graph)

    print(num_paths)
