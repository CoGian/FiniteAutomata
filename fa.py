import re
import sys
import os
from utils import parse_file
from automata import Automaton

"""Usage : python fa.py <automaton description>"""


def main():
    try:
        file_to_read = sys.argv[1]
    except IndexError:
        print("Enter valid command arguments !" + '\n' + "Usage : python fa.py <automaton description>")
        exit(0)

    data_folder = os.path.join("automaton descriptions")

    file_to_open = os.path.join(data_folder, file_to_read)
    try:
        with open(file_to_open, 'r', encoding="utf8") as f:
            num_of_states, start, finish, transitions = parse_file(f)
            print(num_of_states, start, finish, transitions)
            a = Automaton(num_of_states, start, finish, transitions)
            word = "1100"
            for letter in word:
                a.step(letter)
                print(a.current_states)
    except EnvironmentError:
        print("File not found!")


if __name__ == '__main__':
    main()
