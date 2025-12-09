import sys


def get_tiles():
    tiles = [line.strip().split(',') for line in sys.stdin]
    tiles = [map(int, tile) for tile in tiles]
    tiles = [tuple(tile) for tile in tiles]

    return tiles


def get_area(x1, y1, x2, y2):
    width = abs(x1-x2) + 1
    height = abs(y1-y2) + 1

    area = width * height

    return area


if __name__ == '__main__':
    tiles = get_tiles()

    n = len(tiles)

    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            area = get_area(*tiles[i], *tiles[j])
            max_area = max(area, max_area)

    print(max_area)
