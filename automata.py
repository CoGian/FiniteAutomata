class Automaton(object):

    def __init__(self, num_of_states, start, finish, transitions):
        self.num_of_states = num_of_states
        self.start = start
        self.finish = finish
        self.transitions = transitions
        self.current_states = []
        self.current_states.append(start)
        self.add_e_transitions(start)

        print(self.current_states)

    def step(self, letter):

        temp_current_states = []
        for s in self.current_states:
            automaton_dict = self.transitions[s-1]
            # check if transition for letter exists
            if letter in automaton_dict:
                # do the transition
                temp_current_states.extend(automaton_dict[letter])

        if not temp_current_states:
            print("fail")
        else:
            self.current_states = temp_current_states
            for s in temp_current_states:
                self.add_e_transitions(s)

        if not temp_current_states:
            print("fail")
        else:
            self.current_states = temp_current_states

    def add_e_transitions(self, state):
       pass
