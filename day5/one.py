import sys


input = sys.stdin.read()


def parse_range(range_str):
    start, end = range_str.split('-')
    return int(start), int(end)


def get_ranges():
    ranges_str, _ = input.split('\n\n')
    ranges_strs = ranges_str.split()
    ranges = []
    for range_str in ranges_strs:
        range = parse_range(range_str)
        ranges.append(range)

    return ranges


def get_ingredient_ids():
    _, ingredient_ids = input.split('\n\n')
    ingredient_ids = [line.strip() for line in ingredient_ids.split()]
    ingredient_ids = map(int, ingredient_ids)

    return list(ingredient_ids)


if __name__ == '__main__':
    ranges = get_ranges()
    ingredient_ids = get_ingredient_ids()

    num_fresh = 0
    for ingredient_id in ingredient_ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                num_fresh += 1
                break

    print(num_fresh)

