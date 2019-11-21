# FiniteAutomata

Usage : python fa.py <automaton description>
example: python fa.py dfa1.txt
  
in dfa1.txt : 
3 #number of states
1 #initial state
2 3 #final states
1 a 2 # from state 1 to state 2 goes with a 
1 b 1
2 a 3
2 b 1
3 a 3
3 b 1

# the symbol @ is for ε transitions
