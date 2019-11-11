import re


def parse_file(file):
    # read number of states
    line = file.readline()
    num_of_states = int(re.split("[\n]", line)[0])

    # read start state
    line = file.readline()
    start = int(re.split("[\n]", line)[0])

    # read finish states
    line = file.readline()
    temp_finish = re.split("[ '\'\n]", line)
    finish = []
    for c in temp_finish:
        if c is '':
            break
        finish.append(int(c))

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

    return num_of_states, start, finish, transitions
