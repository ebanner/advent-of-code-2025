import sys


def get_banks():
    banks = [line.strip() for line in sys.stdin]
    return banks


def find_max_digit(bank):
    max_digit = -1
    for j, joltage in enumerate(bank):
        if int(joltage) > max_digit:
            max_digit = int(joltage)
            i = j
    return i, str(max_digit)



def get_max_voltage(bank):
    i, j1 = find_max_digit(bank)
    if i == len(bank) - 1:
        _, j2 = find_max_digit(bank[:-1])
        return int(j2+j1)
    else:
        _, j2 = find_max_digit(bank[i+1:])
        return int(j1+j2)



if __name__ == '__main__':
    banks = get_banks()

    max_voltages_sum = 0
    for bank in banks:
        max_voltage = get_max_voltage(bank)
        max_voltages_sum += max_voltage

    print(max_voltages_sum)

