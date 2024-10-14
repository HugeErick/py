# Gauss Implementation
# Erick Gonzalez Parada

import numpy as np

# declaration

#A = np.array([[1,1,1], [2,3,-1], [6, -2, -3]])
#B = np.array([[6], [5], [-7]])

#e.g. 1 : one sol
A = np.array([[3.,-2], [5, 2]])
B = np.array([[4.], [12]])

#e.g. 2 : infinite sol
A2 = np.array([[1, -1], [2, -2]])
B2 = np.array([[7], [14]])

#e.g. 3 : no sol
A3 = np.array([[1, -1], [2, -2]])
B3 = np.array([[7], [10]])

print("print matrix A")
print(A)

print("Size of A")
print(np.shape(A))
print("Dimension")
print(np.ndim(A))
print("num of rows")
print(np.shape(A)[0])
print("num of cols")
print(np.shape(A)[1])

print("print matrix B")
print(B)

print("Size of B")
print(np.shape(B))
print("Dimension")
print(np.ndim(B))
print("num of rows")
print(np.shape(B)[0])
print("num of cols")
print(np.shape(B)[1])

# Augmented Matrix

C = np.concatenate((A,B), axis=1)
print(type(C))
print("Augmented matrix")
print(C)
print("size of C ", np.shape(C))
print("rows: ", np.shape(C)[0])
print("cols: ", np.shape(C)[1])

# Solving
# this works only when det(A) != 0
# Add if statement if this doesnt work
x = np.linalg.solve(A, B)
print("\nSol:\n\n", x)

for j in range(np.shape(C)[0]):
    print('col: ', j)
    for i in range(np.shape(C)[1]):
        print("row: ", i)

print("=========================")

for j in range(np.shape(C)[1] -1):
    print("--------------------")
    print("col: ", j)
    if C[j, j] != 1 and C[j, j] != 0:
        C[j, :] = C[j, :]/C[j, j]
        print(C[j, :])
    else:
        print("pivot equals 1, row not modified")
        print(C[j, :])

    for i in range(np.shape(C)[0]):
        print("row: ", i)
        if i != j:
            C[i, :] = C[i, :] - C[i, j]*C[j, :]
            print(C[i, :])
            print("modified matrix C\n", C)
        else:
            print("the index are the same")
            print("modified matrix C\n", C)

