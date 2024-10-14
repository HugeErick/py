import numpy as np

A = np.array([[2, -3 ,1], [1, -1, 2], [3, 1, -1]])

b = np.array([-1, -3, 9])

x = np.linalg.solve(A, b)

print("res: ", x)

detA = np.linalg.det(A)

print("determinant of A: ", detA)
