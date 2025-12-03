import sys


def get_banks():
    lines = [line.strip() for line in sys.stdin]
    banks = [list(map(int, line)) for line in lines]
    return banks


def argmax(bank, r, l):
    max = 0
    max_i = -1
    for i in range(r, l-1, -1):
        if bank[i] >= max:
            max = bank[i]
            max_i = i

    return max_i, max


def get_max_voltage(bank):
    l = 0
    digits = []
    for digit_idx in range(12):
        r = len(bank) - (12-digit_idx)
        i, digit = argmax(bank, r, l)
        digits.append(digit)
        l = i + 1

    max_voltage = int(''.join(str(digit)for digit in digits))

    return max_voltage


if __name__ == '__main__':
    banks = get_banks()

    max_voltages_sum = 0
    for bank in banks:
        max_voltage = get_max_voltage(bank)
        max_voltages_sum += max_voltage

    print(max_voltages_sum)

