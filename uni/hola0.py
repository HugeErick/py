# Practica 1

# nombre: Erick Gonzalez

# Materia: Analisis numerico

# secc: 1


print("Hola mundo!")

###############################

a = 8
b = 9
c = a + b
print(c)

#############################

a = "8"
b = "9"
c = a + b
print(c)

#############################

a = 8.
b = 9.
c = a + b
print(c)

a = 8
b = 9
c = a + b
print(type(c))

## Metodos numericos

import numpy as np

print(np.sign(5))
print(np.abs(-5))

def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = (a + b)/2

    if (np.abs(f(m)))<tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)

print("\n Example 1 \n")

f = lambda x: x**2 -2

root = my_bisection(f, 0, 2, 0.1)
print("Solution:", root)




