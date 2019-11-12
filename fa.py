try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import sys
import os
from utils import parse_file
from automata import FiniteAutomaton
from insertgui import InsertGUI


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
            # parsing of file
            num_of_states, initial, final_states, transitions = parse_file(f)
            # initialization of automaton
            automaton = FiniteAutomaton(num_of_states, initial, final_states, transitions)
            # initialize Insert GUI
            root = tk.Tk()
            insert_gui = InsertGUI(root, automaton)
            root.mainloop()
    except EnvironmentError:
        print("File not found!")


if __name__ == '__main__':
    main()

