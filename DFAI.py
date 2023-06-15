# a program to implement a Deterministic Finite Automata with given parameters


# Class representing a finite state automata
class Automata:
    def __init__(self, alphabet, stateSet, start, finalSet) -> None:
        self.alphabet = alphabet
        self.stateSet = {}
        self.finalSet = finalSet
        for s in stateSet:
            self.stateSet[s] = State(s)
            if s == start: 
                self.start = self.stateSet[s]
            
            
        self.head = start
    
    # check the final state and condition of exit
    def check_final(self, state):
        if state.name in self.finalSet:
            return True
        return False
    
    # define a new rule for automata
    def add_new_rule(self, input, currState, nextState):
        self.stateSet[currState].add_rule(input, nextState)
        
    def validate(self, input):
        i = len(input)
        for c in input:
            #check final state on last input
            if i == len(input) - 1:
                if self.check_final(self.head):
                    return True
                return False
            
            
        
#Class representing a state of the automata
class State:
    def __init__(self, name) -> None:
        self.name = name
        self.rules = {}

    #add new rule for going to the next state
    def add_rule(self, input, next):
        self.rules[input] = next
    
    #get the next state based on input
    def next_state(self, input):
        return self.rules[input]
            
            