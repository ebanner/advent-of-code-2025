import math
import sys


def transpose(grid):
    return [list(col) for col in zip(*grid)]


def get_problems():
    grid = [line.split() for line in sys.stdin]
    problems = transpose(grid)
    return problems


def parse(problem):
    operands, operation = map(int, problem[:-1]), problem[-1]
    return list(operands), operation


def solve(problem):
    operands, operation = parse(problem)
    if operation == '+':
        result = sum(operands)
    elif operation == '*':
        result = math.prod(operands)

    return result


if __name__ == '__main__':
    problems = get_problems()

    grand_total = 0
    for problem in problems:
        result = solve(problem)
        grand_total += result

    print(grand_total)
