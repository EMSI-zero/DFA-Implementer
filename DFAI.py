# a program to implement a Deterministic Finite Automata with given parameters
import re

# Class representing a finite state automata
class Automata:
    def __init__(
        self, alphabet: list[str], stateSet: list[str], start: str, finalSet: list[str]
    ) -> None:
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
    def add_new_rule(self, currState: str, input: str, nextState: str):
        if currState not in self.stateSet:
            print(currState)
            return "state  does not exist"
        if nextState not in self.stateSet:
            return "next state  does not exist"
        if input not in self.alphabet:
            return "input not in alphabet"
        self.stateSet[currState].add_rule(input, self.stateSet[nextState])
        return "rule added"

    #Accepting an input
    def validate(self, input: str):
        for i in range(-1,len(input)):
            i += 1
            
            # check final state on last input
            if i == len(input) or len(input) == 0:
                if self.check_final(self.head):
                    return True
                self.reset_automata()
                return False
            elif self.head.next_state(input[i]) != "":
                self.head = self.stateSet[self.head.next_state(input[i])]
            else:
                self.reset_automata()
                return False

        self.reset_automata()
        return False

    #set current state to initial state
    def reset_automata(self):
        self.head = self.start

# Class representing a state of the automata
class State:
    def __init__(self, name) -> None:
        self.name = name
        self.rules = {}

    # add new rule for going to the next state
    def add_rule(self, input, next):
        self.rules[input] = next

    # get the next state based on input
    def next_state(self, input):
        if input in self.rules:
            return self.rules[input].name
        else:
            return ""

inputFile = open("DFA_input_1.txt", "r")
lines = inputFile.readlines()
lNum = 0
alphabet = []
states = []
start = ""
finalStates = []
rules = []
for l in lines:
    match (lNum):
        case 0:
            alphabet = re.split(' |\n', l)[:-1]
            print(alphabet)
        case 1:
            states = re.split(' |\n',l)[:-1]
            print(states)
        case 2:
            start = re.split(' |\n', l)[0]
            print(start)
        case 3:
            finalStates = re.split(' |\n', l)[:-1]
            print(finalStates)
        case _:
            rule = re.split(' |\n', l)
            rules.append(rule)
    lNum += 1

dfa = Automata( alphabet, states, start, finalStates)
for rule in rules:
    print(dfa.add_new_rule(rule[0], rule[1], rule[2]))


print(dfa.validate("aaa"))
print(dfa.validate("a"))
print(dfa.validate("b"))
print(dfa.validate("aba"))
print(dfa.validate("aaaaaaab"))
print(dfa.validate("abaaaaaa"))
