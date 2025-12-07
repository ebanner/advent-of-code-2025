import sys


NUM_SPLIT = 0


def get_grid():
    grid = [list(line) for line in sys.stdin]
    return grid


def get_start(grid):
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                return (i, j)


def get_next(i, j, grid):
    if i == len(grid) - 1:
        return []

    elif grid[i+1][j] == '|':
        return []

    elif grid[i+1][j] == '.':
        grid[i+1][j] = '|'
        return [(i+1, j)]

    elif grid[i+1][j] == '^':
        global NUM_SPLIT
        NUM_SPLIT += 1
        grid[i+1][j-1], grid[i+1][j+1] = '|', '|'
        return [(i+1, j-1), (i+1, j+1)]


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

    print(NUM_SPLIT)
