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


def try_remove_roll(grid, i, j):
    if grid[i][j] == '.':
        return

    if not is_accessible(grid, i, j):
        return

    grid[i][j] = '.'


def get_num_rolls(grid):
    n, m = len(grid), len(grid[0])

    num_rolls = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                num_rolls += 1

    return num_rolls


def try_remove_rolls(grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue

            try_remove_roll(grid, i, j)

    return get_num_rolls(grid)


if __name__ == '__main__':
    grid = get_grid()

    n, m = len(grid), len(grid[0])

    orig_num_rolls = get_num_rolls(grid)

    prev_num_rolls = 0
    while True:
        num_rolls = try_remove_rolls(grid)
        if num_rolls == prev_num_rolls:
            break

        prev_num_rolls = num_rolls

    num_rolls = get_num_rolls(grid)
    num_rolls_removed = orig_num_rolls - num_rolls

    print(num_rolls_removed)
