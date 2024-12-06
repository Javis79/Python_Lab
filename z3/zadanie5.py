class Transition:
    def __init__(self, next_state, output):
        self.next_state = next_state
        self.output = output

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def next_state(self, input_state, next_state, output):
        self.transitions[input_state] = Transition(next_state, output)

    def get_transition(self, input_state):
        return self.transitions.get(input_state)


class Mealy:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def processing_data(self, input_state):
        transition = self.current_state.get_transition(input_state)
        if not transition:
            raise ValueError("Brak przejścia")

        output = transition.output
        self.current_state = transition.next_state
        return output

state_a = State("A")
state_b = State("B")

state_a.next_state('0', state_a, 'A')
state_a.next_state('1', state_b, 'B')
state_b.next_state('0', state_b, 'B')
state_b.next_state('1', state_a,  'A')


inputs = ['1','1', '0', '0', '1', '1', '0', '1' ]
outputs = []

mealy_m = Mealy(state_a)

print("Stan początkowy: ", mealy_m.current_state.name)
for inp in inputs:
    output = mealy_m.processing_data(inp)
    outputs.append(output)
    print(f"Wejście: {inp}, Wyjście: {output}, Stan: {mealy_m.current_state.name}")

print("\nSekwencja wyjść:", outputs)
