import numpy as np

np.random.seed(10)
A = np.random.randint(1,10,size = (3,3))
B = np.random.randint(1,10,size = (3,2))

def multiply_matrix(a,b):
    if a.shape[1] == b.shape[0]:
        c = np.zeros((a.shape[0], b.shape[1]), dtype=int)
        for row in range(a.shape[0]):
            for col in range(b.shape[1]):
                for elt in range(b.shape[0]):
                    c[row, col] += a[row, elt] * b[elt, col]
        return c
    else:
        return "Sorry, cannot multiply A and B."


print(f"Matrix A:\n{A}")
print(f"Matrix B:\n {B}")

print("Result:\n",multiply_matrix(A, B))