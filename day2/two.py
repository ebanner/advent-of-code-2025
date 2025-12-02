import itertools
import sys


def parse_range_str(range_str):
    start, end = range_str.split('-')
    return int(start), int(end)


def get_id_ranges():
    line = sys.stdin.readline()
    range_strs = line.split(',')

    ranges = []
    for range_str in range_strs:
        range = parse_range_str(range_str)
        ranges.append(range)

    return ranges


def is_invalid(id):
    str_id = str(id)
    id_len = len(str_id)

    for i in range(1, id_len):
        if id_len % i != 0:
            continue

        batches = list(itertools.batched(str_id, i))
        if all(batch == batches[0] for batch in batches):
            return True

    return False


if __name__ == '__main__':
    id_ranges = get_id_ranges()

    invalid_ids_sum = 0
    for start, end in id_ranges:
        for id in range(start, end+1):
            if is_invalid(id):
                invalid_ids_sum += id

    print(invalid_ids_sum)
