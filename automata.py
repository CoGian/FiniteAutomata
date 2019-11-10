
class automaton(object):

    def __init__(self, num_of_states, start, num_of_finishes, finish, transitions):
        self.num_of_states = num_of_states
        self.start = start
        self.num_of_finishes = num_of_finishes
        self.finish = finish
        self.transitions = transitions
        self.current_states = []


