class AFN():
    def __init__(self, InState, FnState, numStates, transitions, states):
        self.epsilon = "ε"
        self.numStates = numStates
        
        self.states = states
        self.initialState = InState
        self.finalState = FnState
        self.transitions = transitions
    
    def __str__(self):
        return f"No. Estados: {self.numStates}\nEstados: {self.states}\nEstado inicial: {self.initialState}\nEstado final: {self.finalState}\nTransiciones: {self.transitions}"