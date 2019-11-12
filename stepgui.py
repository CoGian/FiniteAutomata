import sys
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


class StepGUI:
    def __init__(self, master, word, automaton):
        self.word = word
        self.automaton = automaton
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        master.geometry("365x169+445+392")
        master.minsize(120, 1)
        master.maxsize(1684, 1031)
        master.resizable(1, 1)
        master.title("Finite Automaton")
        master.configure(background="#c0c0c0")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.Step = tk.Button(master)
        self.Step.place(relx=0.10, rely=0.060, height=24, width=104)
        self.Step.configure(activebackground="#ececec")
        self.Step.configure(activeforeground="#000000")
        self.Step.configure(background="#d9d9d9")
        self.Step.configure(disabledforeground="#a3a3a3")
        self.Step.configure(foreground="#000000")
        self.Step.configure(highlightbackground="#d9d9d9")
        self.Step.configure(highlightcolor="black")
        self.Step.configure(pady="0")
        self.Step.configure(text='''Step''')
        self.Step.configure(command = self.onstep)

        self.Listbox1 = tk.Listbox(master)
        self.Listbox1.place(relx=0.10, rely=0.470, relheight=0.426
                , relwidth=0.100)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.insert('end', *automaton.current_states)

        self.Label2 = tk.Label(master)
        self.Label2.place(relx=0.10, rely=0.296, height=21, width=80)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Current States''')

        self.Label3 = tk.Label(master)
        self.Label3.place(relx=0.4, rely=0.3, height=21, width=114)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Remaining word:''')

        self.TLabel1 = ttk.Label(master)
        self.TLabel1.place(relx=0.4, rely=0.4, height=19, width=115)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text=self.word)

        self.Label1 = tk.Label(master)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")

    def onstep(self):
        # take the first letter of the word
        letter = self.word[0]
        # update remaining word
        self.word = self.word[1:]
        self.TLabel1.configure(text=self.word)
        # do a step for a letter
        self.automaton.step(letter)
        # update listbox
        self.Listbox1.delete(0, 'end')
        self.Listbox1.insert('end', *self.automaton.current_states)
        # check if the word is accepted by automaton
        if not self.word:
            fail = True
            finish_states = []
            for state in self.automaton.current_states:
                if state in self.automaton.finish:
                    finish_states.append(state)
                    # print success
                    self.Label1.place(relx=0.4, rely=0.70, height=21, width=180)
                    self.Label1.configure(foreground="green")
                    self.Label1.configure(text="Accepted!!!Finish States " + str(finish_states))
                    fail = False
            if fail:
                self.Label1.place(relx=0.4, rely=0.70, height=21, width=180)
                self.Label1.configure(foreground="red")
                self.Label1.configure(text="Declined...")
            self.Step.place_forget()





    def start_insert_gui(self):
        word = self.Entry1.get()
        self.master.destroy()
        root = tk.Tk()
        step_gui = StepGUI(root, word, self.automaton)
        root.mainloop()

