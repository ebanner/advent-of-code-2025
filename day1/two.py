import sys


def get_rotations():
    rotations = [line for line in sys.stdin]
    return rotations


def parse_rotation(rotation):
    direction, magnitude = rotation[0], rotation[1:]
    return direction, int(magnitude)


if __name__ == '__main__':
    rotations = get_rotations()

    dial = 50
    zeros = 0
    for rotation in rotations:
        direction, magnitude = parse_rotation(rotation)

        if direction == 'R':
            for _ in range(magnitude):
                dial += 1
                dial %= 100
                if dial == 0:
                    zeros += 1

        elif direction == 'L':
            for _ in range(magnitude):
                dial -= 1
                dial %= 100
                if dial == 0:
                    zeros += 1

    password = zeros
    print(password)

