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


def will_fit(shapes, dimensions, shapes_count):
    def get_area(width, height):
        return width*height

    def get_shape_area(shapes):
        shape = shapes[0]
        shape_area = 0
        for row in shape:
            shape_area += len(row)
        return shape_area


    grid_area = get_area(*dimensions)

    shape_area = get_shape_area(shapes)

    shapes_area = 0
    for shape_count in shapes_count:
        for shape in range(shape_count):
            shapes_area += shape_area

    return shapes_area <= grid_area


if __name__ == '__main__':
    shapes = get_shapes()
    regions = get_regions()

    num_fit = 0
    for region in regions:
        result = will_fit(shapes, *region)
        num_fit += result

    print(num_fit)
