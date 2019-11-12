import re


def parse_file(file):
    # read number of states
    line = file.readline()
    num_of_states = int(re.split("[\n]", line)[0])

    # read initial state
    line = file.readline()
    initial = int(re.split("[\n]", line)[0])

    # read final_states states
    line = file.readline()
    temp_final_states = re.split("[ '\'\n]", line)
    final_states = []
    for c in temp_final_states:
        if c is '':
            break
        final_states.append(int(c))

    # read transitions
    transitions = [None] * num_of_states
    # transitions will be a list of dictionaries which have list as a value
    while True:
        line = file.readline()
        if not line:
            break
        line = re.split("[ '\'\n]", line)

        current_state = int(line[0])
        symbol = line[1]
        next_state = int(line[2])
        if transitions[current_state-1] is None:
            transition = {symbol: [next_state]}
            transitions[current_state-1] = transition
        else:
            if symbol in transitions[current_state-1]:
                transitions[current_state - 1][symbol].append(next_state)
            else:
                transitions[current_state - 1][symbol] = [next_state]

    return num_of_states, initial, final_states, transitions
