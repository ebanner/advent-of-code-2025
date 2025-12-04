import sys


def get_grid():
    grid = [list(line.strip()) for line in sys.stdin]
    return grid


def get(grid, i, j):
    n, m = len(grid), len(grid[0])

    if 0 <= i < n and 0 <= j < m:
        return grid[i][j]
    else:
        return '.'


def is_accessible(grid, i, j):
    num_rolls = 0

    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == dj == 0:
                continue

            if get(grid, i+di, j+dj) == '@':
                num_rolls += 1

    return num_rolls < 4


if __name__ == '__main__':
    grid = get_grid()

    n, m = len(grid), len(grid[0])

    num_accessible = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue

            if is_accessible(grid, i, j):
                num_accessible += 1

    print(num_accessible)
