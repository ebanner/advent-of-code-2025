import math
import sys


def transpose(grid):
    return [list(col) for col in zip(*grid)]


def get_problem_grid():
    problem_grid = [list(line.rstrip('\n')) for line in sys.stdin]
    return problem_grid


def parse(problem):
    grid, operand_list = problem[:-1], problem[-1]

    transposed_grid = transpose(grid)
    operands = [int(''.join(row).strip()) for row in transposed_grid]

    operator = operand_list[0]

    return operands, operator


def solve(problem):
    operands, operation = parse(problem)
    if operation == '+':
        result = sum(operands)
    elif operation == '*':
        result = math.prod(operands)

    return result


def find_next_operand(problem_grid, j):
    n, m = len(problem_grid), len(problem_grid[0])

    k = j
    while k < m and problem_grid[n-1][k] == ' ':
        k += 1

    return k if k < m else k+1


def get_problems(problem_grid):
    n, m = len(problem_grid), len(problem_grid[0])

    operand_row = problem_grid[n-1]

    for j in range(m):
        if problem_grid[n-1][j] == ' ':
            continue

        k = find_next_operand(problem_grid, j+1)
        problem = [row[j:k-1] for row in problem_grid]

        yield problem


if __name__ == '__main__':
    problem_grid = get_problem_grid()

    grand_total = 0
    for problem in get_problems(problem_grid):
        result = solve(problem)
        grand_total += result

    print(grand_total)
