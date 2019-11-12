class FiniteAutomaton(object):

    def __init__(self, num_of_states, initial, final_states, transitions):
        self.num_of_states = num_of_states
        self.initial = initial
        self.final_states = final_states
        # a list of dictionaries which have list of the states in which the automaton will go as a value
        self.transitions = transitions
        self.current_states = []
        self.current_states.append(initial)
        # do e transitions
        if '@' in self.transitions[initial - 1]:
            self.do_e_transitions(initial)

    # reload initial configuration
    def reload(self):
        self.current_states = []
        self.current_states.append(self.initial)
        # do e transitions
        if '@' in self.transitions[self.initial - 1]:
            self.do_e_transitions(self.initial)

    def step(self, letter):

        temp_current_states = []
        for s in self.current_states:
            automaton_dict = self.transitions[s-1]
            # check if state has any transition
            if not automaton_dict:
                pass
            # check if transition for letter exists
            elif letter in automaton_dict:
                # do the transition
                temp_current_states.extend(automaton_dict[letter])

        self.current_states = temp_current_states
        if self.current_states:
            # do e transitions if they exist
            for s in self.current_states:
                automaton_dict = self.transitions[s-1]
                if not automaton_dict:
                    pass
                elif '@' in self.transitions[s-1]:
                    self.do_e_transitions(s)
        if not self.current_states:
            print("fail")

    # check recursively for e transitions of a state and make them
    def do_e_transitions(self, state):
        next_states = self.transitions[state-1]['@']
        for s in next_states:
            if s not in self.current_states:
                self.current_states.append(s)
            automaton_dict = self.transitions[s - 1]
            if not automaton_dict:
                pass
            elif '@' in self.transitions[s - 1]:
                self.do_e_transitions(s)


