# a program to implement a Deterministic Finite Automata with given parameters


# Class representing a finite state automata
class Automata:
    def __init__(self, alphabet : list[str], stateSet : list[str], start : str, finalSet : list[str]) -> None:
        self.alphabet = alphabet
        self.stateSet = {}
        self.finalSet = finalSet
        for s in stateSet:
            self.stateSet[s] = State(s)
            if s == start: 
                self.start = self.stateSet[s]
            
            
        self.head = self.start
    
    # check the final state and condition of exit
    def check_final(self, state):
        if state.name in self.finalSet:
            return True
        return False
    
    # define a new rule for automata
    def add_new_rule(self, input : str, currState : str, nextState : str):
        if currState not in self.stateSet:
            return "state  does not exist"
        if nextState not in self.stateSet:
            return "next state  does not exist"
        self.stateSet[currState].add_rule(input, self.stateSet[nextState])
        return "rule added"
        
    def validate(self, input: str):
        i = 0
        for c in input:
            #check final state on last input
            if i == len(input)-1:
                if self.check_final(self.head):
                    return True
                return False
            if self.head.next_state(c) != "":
                self.head = self.stateSet[self.head.next_state(c)]
            else:
                return False
            i+= 1
        
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
    def next_state(self, input) : 
        if input in self.rules:
            return self.rules[input].name
        else: 
            return ""
            

dfa = Automata(["a","b"], ["q1","q2"], "q1", ["q2"])

print(dfa.add_new_rule("a", "q1", "q2"))
print(dfa.add_new_rule("a", "q2", "q2"))

print(dfa.validate("aaa"))
print(dfa.validate("aba"))
print(dfa.validate("aaaaaaaab"))
print(dfa.validate("abaaaaaa"))
