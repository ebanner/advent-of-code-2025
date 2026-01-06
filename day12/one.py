import sys


input = sys.stdin.read()


def get_shapes():
    def parse(shape_str):
        shape_strs = shape_str.split('\n')[1:]
        shape = [list(shape_str) for shape_str in shape_strs]
        return shape

    shape_strs = input.split('\n\n')[:-1]
    shapes = []
    for shape_str in shape_strs:
        shape = parse(shape_str)
        shapes.append(shape)

    return shapes


def get_regions():
    def parse(region_str):
        size, shape_idxs = region_str.split(':')
        size, shape_idxs = size.split('x'), shape_idxs.strip().split()
        size, shape_idxs = map(int, size), map(int, shape_idxs)
        return (tuple(size), list(shape_idxs))

    chunk = input.split('\n\n')[-1]
    region_strs = [line.strip() for line in chunk.split('\n') if line]
    regions = [parse(region_str) for region_str in region_strs]

    return regions


def get_grid(width, height):
    grid = [['.']*width for _ in range(height)]
    return grid


def all_zeros(shapes_count):
    return all(shape_count == 0 for shape_count in shapes_count)


def zeros(A):
    n = len(A)
    A_zero = [[0]*n for row in A]
    return A_zero


def rot90(A):
    n = len(A)

    A_rot = zeros(A)
    for k in range(n-1, -1, -1):
        I, J = range(n), range(n)
        for i, j in zip(I, J): 
            A_rot[i][k] = A[n-k-1][j]
            A_rot[i][k] = A[n-k-1][j]

    return A_rot


def rot180(A):
    A_rot = rot90(A)
    A_rot_rot = rot90(A_rot)
    return A_rot_rot


def rot270(A):
    A_rot_rot = rot180(A)
    A_rot_rot_rot = rot90(A_rot_rot)
    return A_rot_rot_rot


def copy(A):
    A_copy = [row[:] for row in A]
    return A_copy


def reflect(A):
    n, m = len(A), len(A[0])

    A_reflected = copy(A)

    def swap_col(j):
        for i in range(n):
            A_reflected[i][j], A_reflected[i][m-1-j] = A_reflected[i][m-1-j], A_reflected[i][j]

    for j in range(m // 2):
        swap_col(j)

    return A_reflected


def get_orientations(shape):
    transforms = [
        lambda x: x,
        rot90,
        rot180,
        rot270,
        lambda x: rot90(reflect(x)),
        lambda x: rot180(reflect(x)),
        lambda x: rot270(reflect(x))
    ]

    orientations = [transform(shape) for transform in transforms]
    return orientations


def can_place(placement, offset_i, offset_j, grid):
    n, m = len(placement), len(placement[0])

    for i in range(n):
        for j in range(m):
            if placement[i][j] == '.':
                continue

            try:
                if grid[offset_i+i][offset_j+j] != '.':
                    return False
            except IndexError:
                return False

    return True


def get_placements(shape, grid):
    orientations = get_orientations(shape)

    n, m = len(grid), len(grid[0])

    placements = []
    for orientation in orientations:
        for i in range(n):
            for j in range(m):
                placement = (orientation, i, j)
                if can_place(*placement, grid):
                    placements.append(placement)

    return placements


def place(shape, offset_i, offset_j, grid):
    n, m = len(shape), len(shape[0])

    grid_copy = copy(grid)

    for i in range(n):
        for j in range(m):
            if shape[i][j] == '#':
                grid_copy[offset_i+i][offset_j+j] = '#'

    return grid_copy


def will_fit(shapes, size, shapes_count):
    def get_next_shape(shapes_count):
        for shape_idx, shape_count in enumerate(shapes_count):
            if shape_count > 0:
                return shape_idx, shapes[shape_idx]

    def search(shapes_count, grid):
        # print('search', shapes_count)
        # for row in grid:
        #     print(''.join(row))
        # print()

        if all_zeros(shapes_count):
            return True

        shape_idx, shape = get_next_shape(shapes_count)
        placements = get_placements(shape, grid)
        for placement in placements:
            new_grid = place(*placement, grid)
            new_shapes_count = shapes_count[:]
            new_shapes_count[shape_idx] -= 1
            if search(new_shapes_count, new_grid):
                return True

        return False

    grid = get_grid(*size)
    result = search(shapes_count, grid)

    return result


if __name__ == '__main__':
    shapes = get_shapes()
    regions = get_regions()

    for shape in shapes:
        for row in shape:
            print(''.join(row))
        print()

    for region in regions:
        print(region)
    print()

    num_fit = 0
    for region in regions:
        result = will_fit(shapes, *region)
        num_fit += result

    print(num_fit)
