# reporte array  
# nombre: Erick Gonzalez Parada
# materia: analisis numerico
# seccion: 1

import numpy as np
# declaration
a = ['r', 'o', 'o', 't']
b = np.array([34, 76, 91, 191, 2, 853, 36, 85, 99, 467])
c = ['a', 'n', 's']
bAprox = np.array([34.1, 76.1, 91.1, 191.1, 2.1, 853.1, 36.1, 85.1, 99.1, 467.1])
# Accessing array
e1 = b[0]
e4 = b[3]

x = np.linspace(0, 2, 3)

print('lol', x)

print(type(x))
np.ndarray

print(type(x[0]))


# zeros function

x = np.zeros(3, int)

y = np.zeros(3)

print(y)
print(len(y))

# array function

x = np.array([0, 1, 2])
print(x)

x = np.array([0., 1., 2.])
print(x)

# activity
print(np.abs(b - bAprox))

# matrix

# nested lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)

# using numpy
matrix = np.array([[1,2,3], [4,5,6], [7, 8, 9]])
print(matrix)

el00 = matrix[0][0]
el22 = matrix[2][2]

print("value at index [0][0]: ", el00 )
print("value at index [3][3]: ", (matrix[3][3]) )
