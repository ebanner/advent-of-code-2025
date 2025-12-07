import sys


def get_grid():
    grid = [list(line.strip()) for line in sys.stdin]

    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                grid[i][j] = 0

    return grid


def get_start(grid):
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                grid[i][j] = 1
                return (i, j)


def get_next(i, j, grid):
    if i == len(grid) - 1:
        return []

    elif grid[i+1][j] == '^':
        grid[i+1][j-1] += grid[i][j]
        grid[i+1][j+1] += grid[i][j]

        return [(i+1, j-1), (i+1, j+1)]

    else:
        grid[i+1][j] += grid[i][j]

        return [(i+1, j)]


def get_num_timelines(grid):
    n = len(grid)

    timelines = grid[n-1]
    num_timelines = sum(timelines)

    return num_timelines


if __name__ == '__main__':
    grid = get_grid()

    start = get_start(grid)
    frontier = set([start])

    while True:
        if not frontier:
            break

        new_frontier = set()
        for node in frontier:
            next = get_next(*node, grid)
            new_frontier.update(next)

        frontier = new_frontier

    num_timelines = get_num_timelines(grid)
    print(num_timelines)
