import sys

import pulp
from tqdm import tqdm


def parse(line):
    tokens = line.split()

    indicator_light_diagram, button_wiring_schematics, joltage_requirements = tokens[0], tokens[1:-1], tokens[-1]

    indicator_light_diagram = tuple(indicator_light_diagram[1:-1])

    button_wiring_schematics = [eval(button_wiring_schematic) for button_wiring_schematic in button_wiring_schematics]
    button_wiring_schematics = [(button_wiring_schematic,) if type(button_wiring_schematic) == int else button_wiring_schematic for button_wiring_schematic in button_wiring_schematics]

    joltage_requirements = joltage_requirements.replace('{', '(').replace('}', ')')
    joltage_requirements = eval(joltage_requirements)

    return indicator_light_diagram, button_wiring_schematics, joltage_requirements


def get_machine_descriptions():
    lines = [line.strip() for line in sys.stdin]
    machine_descriptions = [parse(line) for line in lines]

    return machine_descriptions


def get_A(button_presses, joltages):
    num_buttons = len(joltages)

    A = []
    for button_press in button_presses:
        row = [0]*num_buttons
        for button_idx in button_press:
            row[button_idx] = 1
        A.append(row)

    return A


def get_x(button_presses):
    num_button_presses = len(button_presses)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(num_button_presses)]
    return x


def get_fewest_presses(button_presses, joltages):
    A, x = get_A(button_presses, joltages), get_x(button_presses)
    b = list(joltages)

    problem = pulp.LpProblem("machine", pulp.LpMinimize)
    problem += pulp.lpSum(x)

    num_buttons, num_button_presses = len(joltages), len(button_presses)
    for j in range(num_buttons):
        problem += pulp.lpSum(A[i][j] * x[i] for i in range(num_button_presses)) == b[j]

    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    min_presses = pulp.value(problem.objective)

    return min_presses


if __name__ == '__main__':
    machine_descriptions = get_machine_descriptions()

    sum = 0
    for machine_description in tqdm(machine_descriptions):
        fewest_presses = get_fewest_presses(*machine_description[1:])
        sum += fewest_presses

    print(sum)
