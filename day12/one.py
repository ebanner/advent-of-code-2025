import sys


input = sys.stdin.read()


def get_shapes():
    def parse(shape_str):
        shape = shape_str.split('\n')[1:]
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


def will_fit(shapes, size, shapes_count):
    def search(shapes_count, grid):
        if all_zeros(shapes_count):
            return True

        shape, shape_idx = get_next_shape(shapes_count)
        placements = get_placements(shape)
        for placement in placements:
            if not can_place(shape, grid):
                continue

            new_grid = place(grid)
            new_shapes_count = copy(shapes_count)
            new_shapes_count[shape_idx] -= 1
            if search(new_shapes_count, new_grid):
                return True

        return False


if __name__ == '__main__':
    shapes = get_shapes()
    regions = get_regions()

    for shape in shapes:
        print(shape)
    print()

    for region in regions:
        print(region)
    print()

    num_fit = 0
    for region in regions:
        num_fit += will_fit(shapes, *region)

    print(num_fit)
