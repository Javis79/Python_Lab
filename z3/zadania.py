# zadanie 1
# import numpy as np
#
# np.random.seed(10)
# A = np.random.randint(1,10,size = (3,3))
# B = np.random.randint(1,10,size = (3,2))
#
# def multiply_matrix(a,b):
#     if a.shape[1] == b.shape[0]:
#         c = np.zeros((a.shape[0], b.shape[1]), dtype=int)
#         for row in range(a.shape[0]):
#             for col in range(b.shape[1]):
#                 for elt in range(b.shape[0]):
#                     c[row, col] += a[row, elt] * b[elt, col]
#         return c
#     else:
#         return "Sorry, cannot multiply A and B."
#
#
# print(f"Matrix A:\n{A}")
# print(f"Matrix B:\n {B}")
#
# print("Result:\n",multiply_matrix(A, B))


# zadanie 2
# import json
#
# class Person:
#     def __init__(self, name, surname, address, zipcode, pesel):
#         self.n = name
#         self.s = surname
#         self.a = address
#         self.z = zipcode
#         self.p = pesel
#
#     def save_to_json(self, file):
#         with open(file, 'w', encoding='utf-8') as fil:
#             json.dump(self.__dict__, fil, ensure_ascii=False, indent=4)
#
#     @classmethod
#     def open_from_json(cls, file):
#         with open(file, 'r', encoding='utf-8') as fil:
#             data = json.load(fil)
#
#         mapping = {
#             "n": "name",
#             "s": "surname",
#             "a": "address",
#             "z": "zipcode",
#             "p": "pesel"
#         }
#
#         data2 = {mapping[k]: v for k, v in data.items() if k in mapping}
#         return cls(**data2)
#
#
# x = Person("Jan", "Kowalski", "Krakow 132", "33-103", "123456789012")
# print(x.__dict__)
#
# x.save_to_json("x.json")
# y = Person.open_from_json("x.json")
#
# print(y.__dict__)

# zadanie 5
# class Transition:
#     def __init__(self, next_state, output):
#         self.next_state = next_state
#         self.output = output
#
# class State:
#     def __init__(self, name):
#         self.name = name
#         self.transitions = {}
#
#     def next_state(self, input_state, next_state, output):
#         self.transitions[input_state] = Transition(next_state, output)
#
#     def get_transition(self, input_state):
#         return self.transitions.get(input_state)
#
#
# class Mealy:
#     def __init__(self, initial_state):
#         self.current_state = initial_state
#
#     def processing_data(self, input_state):
#         transition = self.current_state.get_transition(input_state)
#         if not transition:
#             raise ValueError("Brak przejścia")
#
#         output = transition.output
#         self.current_state = transition.next_state
#         return output
#
# state_a = State("A")
# state_b = State("B")
#
# state_a.next_state('0', state_a, 'A')
# state_a.next_state('1', state_b, 'B')
# state_b.next_state('0', state_b, 'B')
# state_b.next_state('1', state_a,  'A')
#
#
# inputs = ['1','1', '0', '0', '1', '1', '0', '1' ]
# outputs = []
#
# mealy_m = Mealy(state_a)
#
# print("Stan początkowy: ", mealy_m.current_state.name)
# for inp in inputs:
#     output = mealy_m.processing_data(inp)
#     outputs.append(output)
#     print(f"Wejście: {inp}, Wyjście: {output}, Stan: {mealy_m.current_state.name}")
#
# print("\nSekwencja wyjść:", outputs)
