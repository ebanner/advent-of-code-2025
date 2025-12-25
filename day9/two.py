import sys


def get_tiles():
    tiles = [line.strip().split(',') for line in sys.stdin]
    tiles = [map(int, tile) for tile in tiles]
    tiles = [tuple(tile) for tile in tiles]

    return tiles


def get_segments(tiles):
    segments = {
        'X': [], 'Y': []
    }

    for (x1, y1), (x2, y2) in zip(tiles, tiles[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        if x1 == x2:
            segment = (x1, y1, y2)
            segments['Y'].append(segment)
        elif y1 == y2:
            segment = (y1, x1, x2)
            segments['X'].append(segment)

    (x1, y1), (x2, y2) = tiles[-1], tiles[0]

    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    if x1 == x2:
        segment = (x1, y1, y2)
        segments['Y'].append(segment)
    elif y1 == y2:
        segment = (y1, x1, x2)
        segments['X'].append(segment)

    return segments


def get_area(x1, x2, y1, y2):
    width = abs(x1-x2) + 1
    height = abs(y1-y2) + 1

    area = width * height

    return area


def cuts(rect_x1, rect_x2, rect_y1, rect_y2, X, Y):
    for (segment_x, segment_y1, segment_y2) in Y:
        if rect_x1 < segment_x < rect_x2 and not (segment_y2 <= rect_y1 or rect_y2 <= segment_y1):
            return True

    for (segment_y, segment_x1, segment_x2) in X:
        if rect_y1 < segment_y < rect_y2 and not (segment_x2 <= rect_x1 or rect_x2 <= segment_x1):
            return True

    return False


def is_outside(rectangle, X, Y):
    def get_midpoint(x1, x2, y1, y2):
        x = (x1+x2) / 2
        y = (y1+y2) / 2
        return (x, y)

    def get_ray(x, y):
        X_max = max(x_max for (_, _, x_max) in X)
        return (y, x, X_max+1)

    def intersects(y, x1, x2, x, y1, y2):
        return x1 < x < x2 and y1 < y < y2

    midpoint = get_midpoint(*rectangle)
    ray = get_ray(*midpoint)

    num_intersections = 0
    for y in Y:
        num_intersections += intersects(*ray, *y)

    if num_intersections % 2 == 1:
        return False
    else:
        return True


def get_rectangle(x1, y1, x2, y2):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    return x1, x2, y1, y2


if __name__ == '__main__':
    tiles = get_tiles()
    perimeter = get_segments(tiles)

    n = len(tiles)

    max_area = 0
    for i in range(n-1):
        for j in range(i+1, n):
            rectangle = get_rectangle(*tiles[i], *tiles[j])

            if cuts(*rectangle, **perimeter):
                continue

            if is_outside(rectangle, **perimeter):
                continue

            area = get_area(*rectangle)
            max_area = max(area, max_area)

    print(max_area)
