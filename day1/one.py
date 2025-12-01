import sys


def get_rotations():
    rotations = [line for line in sys.stdin]
    return rotations


def parse_rotation(rotation):
    direction, magnitude = rotation[0], rotation[1:]
    return direction, int(magnitude)


def rotate(rotation, dial):
    direction, magnitude = parse_rotation(rotation)

    if direction == 'R':
        dial += magnitude
    elif direction == 'L':
        dial -= magnitude

    dial %= 100

    return dial


if __name__ == '__main__':
    rotations = get_rotations()

    dial = 50
    password = 0
    for rotation in rotations:
        dial = rotate(rotation, dial)
        if dial == 0:
            password += 1

    print(password)

