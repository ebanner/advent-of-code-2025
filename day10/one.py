import sys


def parse(line):
    tokens = line.split()

    indicator_light_diagram, button_wiring_schematics, joltage_requirements = tokens[0], tokens[1:-1], tokens[-1]

    indicator_light_diagram = tuple(indicator_light_diagram[1:-1])

    button_wiring_schematics = [eval(button_wiring_schematic) for button_wiring_schematic in button_wiring_schematics]
    button_wiring_schematics = [(button_wiring_schematic,) if type(button_wiring_schematic) == int else button_wiring_schematic for button_wiring_schematic in button_wiring_schematics]

    joltage_requirements = eval(joltage_requirements)

    return indicator_light_diagram, button_wiring_schematics, joltage_requirements


def get_machine_descriptions():
    lines = [line.strip() for line in sys.stdin]
    machine_descriptions = [parse(line) for line in lines]

    return machine_descriptions


def press(button_wiring_schematic, state):
    new_state = list(state[:])
    for button in button_wiring_schematic:
        new_state[button] = '.' if state[button] == '#' else '#'

    return tuple(new_state)


def get_next(state, button_wiring_schematics):
    next_states = []
    for button_wiring_schematic in button_wiring_schematics:
        next_state = press(button_wiring_schematic, state)
        next_states.append(next_state)

    return next_states


def get_empty_indicator_light_diagram(indicator_light_diagram):
    empty_indicator_light_diagram = ('.',)*len(indicator_light_diagram)
    return empty_indicator_light_diagram


def configure(indicator_light_diagram, button_wiring_schematics, joltage_requirements):
    empty_indicator_light_diagram = get_empty_indicator_light_diagram(indicator_light_diagram)

    visited = set()

    frontier = {empty_indicator_light_diagram}
    num_button_presses = 0

    while True:
        if not frontier:
            break

        new_frontier = set()

        for state in frontier:
            if state in visited:
                continue

            visited.add(state)

            if state == indicator_light_diagram:
                return num_button_presses

            states = get_next(state, button_wiring_schematics)
            new_frontier.update(states)

        frontier = new_frontier

        num_button_presses += 1


if __name__ == '__main__':
    machine_descriptions = get_machine_descriptions()

    sum = 0
    for machine_description in machine_descriptions:
        fewest_presses = configure(*machine_description)
        sum += fewest_presses

    print(sum)
