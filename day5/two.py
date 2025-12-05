import sys


input = sys.stdin.read()


def parse_interval(interval_str):
    start, end = interval_str.split('-')
    return int(start), int(end)


def get_intervals():
    intervals_str, _ = input.split('\n\n')
    intervals_strs = intervals_str.split()
    intervals = []
    for interval_str in intervals_strs:
        interval = parse_interval(interval_str)
        intervals.append(interval)

    return intervals


def case1(s1, e1, s2, e2):
    return s2 <= s1 and e1 <= e2

def case2(s1, e1, s2, e2):
    return s1 <= s2 and e2 <= e1


def case3(s1, e1, s2, e2):
    return s2 <= s1 and s1 <= e2 and e2 <= e1


def case4(s1, e1, s2, e2):
    return s1 <= s2 and s2 <= e1 and e1 <= e2


def are_mergable(s1, e1, s2, e2):
    return case1(s1, e1, s2, e2) or case2(s1, e1, s2, e2) or case3(s1, e1, s2, e2) or case4(s1, e1, s2, e2)


def merge_intervals(s1, e1, s2, e2):
    if case1(s1, e1, s2, e2):
        return (s2, e2)
    elif case2(s1, e1, s2, e2):
        return (s1, e1)
    elif case3(s1, e1, s2, e2):
        return (s2, e1)
    elif case4(s1, e1, s2, e2):
        return (s1, e2)


def merge(intervals):
    for i in range(len(intervals)):
        for j in range(i+1, len(intervals)):
            if are_mergable(*intervals[i], *intervals[j]):
                interval = merge_intervals(*intervals[i], *intervals[j])
                del intervals[j]
                del intervals[i]
                intervals.append(interval)
                return


if __name__ == '__main__':
    intervals = get_intervals()

    prev_intervals = intervals[:]
    while True:
        merge(intervals)

        if intervals == prev_intervals:
            break

        prev_intervals = intervals[:]

    num_fresh = 0
    for (start, end) in intervals:
        num_fresh += end - start + 1

    print(num_fresh)
