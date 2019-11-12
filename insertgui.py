
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

from stepgui import StepGUI


class InsertGUI:
    def __init__(self, master, automaton):
        self.automaton = automaton
        self.master = master
        '''This class configures and populates the toplevel window.
                   master is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        master.geometry("221x146+696+359")
        master.minsize(120, 1)
        master.maxsize(1684, 1031)
        master.resizable(1, 1)
        master.title("Input")
        master.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(master)
        self.Entry1.place(relx=0.136, rely=0.274, height=20, relwidth=0.697)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(master)
        self.Label1.place(relx=0.136, rely=0.068, height=21, width=107)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Please type a word:''')

        self.Button1 = tk.Button(master)
        self.Button1.place(relx=0.271, rely=0.548, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Start''')
        self.Button1.configure(command=self.start_step_gui)

    def start_step_gui(self):
        word = self.Entry1.get()
        # destroy Insert GUI
        self.master.destroy()
        # Initialize Step GUI
        root = tk.Tk()
        step_gui = StepGUI(root, word, self.automaton)
        root.mainloop()
