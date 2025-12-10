import sys

from tqdm import tqdm


def get_tiles():
    tiles = [line.strip().split(',') for line in sys.stdin]
    tiles = [map(int, tile) for tile in tiles]
    tiles = [tuple(tile) for tile in tiles]

    return tiles


def contains(perimeter, candidate, tiles):
    def is_corner(tile, tiles):
        return tile in tiles

    def has_north(x, y, perimeter):
        for y_ in range(y, -1, -1):
            if (x, y_) in perimeter:
                return True
        return False

    def has_east(x, y, perimeter):
        for x_ in range(x, 100_000+1):
            if (x_, y) in perimeter:
                return True
        return False

    def has_south(x, y, perimeter):
        for y_ in range(y, 100_000+1):
            if (x, y_) in perimeter:
                return True
        return False

    def has_west(x, y, perimeter):
        for x_ in range(x, -1, -1):
            if (x_, y) in perimeter:
                return True
        return False

    for corner in candidate:
        if not is_corner(corner, tiles) and not (\
                has_north(*corner, perimeter) and \
                has_east(*corner, perimeter) and \
                has_south(*corner, perimeter) and \
                has_west(*corner, perimeter) \
            ):
            # print('no')
            return False

    # print('yes')
    return True


def get_perimeter(tiles):
    perimeter = set()

    for (x1, y1), (x2, y2) in zip(tiles, tiles[1:]):

        if x2 > x1:
            X = range(x1, x2+1)
            Y = [y1]*len(X)
        elif y2 > y1:
            Y = range(y1, y2+1)
            X = [x1]*len(Y)
        elif x2 < x1:
            X = range(x1, x2-1, -1)
            Y = [y1]*len(X)
        elif y2 < y1:
            Y = range(y1, y2-1, -1)
            X = [x1]*len(Y)

        for x, y in zip(X, Y):
            perimeter.add((x, y))

    return perimeter


def get_candidate(x1, y1, x2, y2):
    # print(f'get_candidate({x1}, {y1}, {x2}, {y2})')
    top_left, top_right = (min(x1, x2), min(y1, y2)), (max(x1, x2), min(y1, y2))
    bottom_left, bottom_right = (min(x1, x2), max(y1, y2)), (max(x1, x2), max(y1, y2))

    return [top_left, top_right, bottom_right, bottom_left]


def get_candidates(tiles):
    candidates = []
    for i, (x1, y1) in enumerate(tiles):
        for (x2, y2) in tiles[i+1:]:
            # print(f'{x1},{y1} + {x2},{y2}')
            if x1 <= x2 and y1 <= y2:
                candidate = get_candidate(x1, y1, x2, y2)
            else:
                candidate = get_candidate(x2, y2, x1, y1)

            # print('->', candidate)
            candidates.append(candidate)

    return candidates


def get_area(c1, c2, c3, c4):
    (x1, y1), (x2, y2) = c1, c2
    (x3, y3), (x4, y4) = c3, c4

    width = (x2-x1) + 1
    height = (y3-y1) + 1

    area = width * height

    return area


if __name__ == '__main__':
    tiles = get_tiles()

    print('Getting perimeter...')

    perimeter = get_perimeter(tiles)

    print('done')

    print('Getting candidates...')

    candidates = get_candidates(tiles)

    print('done')

    max_area = 0
    for candidate in tqdm(candidates):
        # print(candidate)
        if contains(perimeter, candidate, tiles):
            area = get_area(*candidate)
            max_area = max(area, max_area)

    print(max_area)
