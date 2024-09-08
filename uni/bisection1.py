# actividad 2 
# nombre: Erick Gonzalez Parada
# materia: analisis numerico
# seccion: 1

import numpy
import sys

def bisection(f, a, b, tol):
    if numpy.sign(f(a)) == numpy.sign(f(b)):
        raise Exception("No root found")
    m = (a + b) / 2

    if numpy.abs(f(m)) < tol:
        return m
    elif numpy.sign(f(a)) == numpy.sign(f(m)):
        return bisection(f, m, b, tol)
    elif numpy.sign(f(b)) == numpy.sign(f(m)):
        return bisection(f, a, m, tol)

# Define the function and call bisection
f = lambda x: x**3 + 4*x**2 - 10
root = bisection(f, 1, 2, 1e-4)

#print("S:", root)

f2 = lambda x: numpy.sqrt(x) - numpy.cos(x)
root2 = bisection(f2, 0, 1, 1e-3)
#print (root2)

fa = lambda x: x - 2**(-x)
fb = lambda x: numpy.e**x - x**2 + 3*x + 2
fc = lambda x: 2*x*numpy.cos(2*x) - (x + 1)**2
fd = lambda x: x*numpy.cos(x) - 2*x**2 + 3*x - 1

roota = bisection (fa, 0 , 1, 1e-5)
rootb = bisection (fb, -1 , 0, 1e-5)
rootc = bisection (fc, -3 , -2, 1e-5)
rootc2 = bisection (fc, -1 , 0, 1e-5)
rootd = bisection (fd, 0.2 , 0.3, 1e-5)
rootd2 = bisection (fd, 1.2 , 1.3, 1e-5)

exit()
print(roota)
print(rootb)
print(rootc)
print(rootc2)
print(rootd)
print(rootd2)
