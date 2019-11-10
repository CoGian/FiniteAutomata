import re
import sys
import os
from utils import parse_file

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
            parse_file(f)

    except EnvironmentError:
        print("File not found!")


if __name__ == '__main__':
    main()
