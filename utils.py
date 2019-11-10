import re


def parse_file(file):
    # read number of states
    line = file.readline()
    num_of_states = int(re.split("[\n]", line)[0])
    print(num_of_states)

    # read number of finish states
    line = file.readline()
    num_of_finishes = int(re.split("[\n]", line)[0])
    print(num_of_finishes)

    # read finish states
    line = file.readline()
    temp_finish = re.split("[ '\'\n]", line)
    finish = []
    for c in temp_finish:
        if c is '':
            break
        finish.append(int(c))
    print(finish)

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
            print(transitions)
        else:
            if symbol in transitions[current_state-1]:
                print(line)
                transitions[current_state - 1][symbol].append(next_state)
            else:
                transitions[current_state - 1][symbol] = [next_state]

    print(transitions)







