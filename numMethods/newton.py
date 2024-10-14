# Actividad 1 
# nombre: Erick Gonzalez Parada
# materia: analisis numerico
# seccion: 1

import numpy as np

def newton(f, Df, x0, epsilon, maxIteration):
    xn = x0
    for n in range(0, maxIteration):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print("found solution after", n, "iterations")
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print("Zero derivative, no solution found")
            return None
        xn = xn - fxn/Dfxn
    print("Exceeded iterations")
    return None

print("\n sample 1")

f = lambda x: x**2 - 2
fPrime = lambda x: 2*x
estimate = newton(f, fPrime, 1.5, 1e-6, 10)
print("estimate = ", estimate)


print("\n sample 2")

f = lambda x: x**3 + 4*x**2 - 10
fPrime = lambda x: 3*x**2 +8*x
estimate = newton(f, fPrime, 1.5, 1e-4, 10)
print("estimate = ", estimate)

print("\n sample 3")

f = lambda x: np.sqrt(x) - np.cos(x)
fPrime = lambda x: (1/(2*np.sqrt(x))) + np.sin(x)
estimate = newton(f, fPrime, 0.5, 1e-3, 10)
print("estimate = ", estimate)

print("\n sample 4")

f = lambda x: x**2 - 10*np.cos(x)
fPrime = lambda x: 2*x +10*np.sin(x)
estimate = newton(f, fPrime, -100, 1e-5, 10)
estimate2 = newton(f, fPrime, 50, 1e-5, 10)
print("estimate = ", estimate)
print("estimate2 = ", estimate2)

print("\n sample 5")

f = lambda x: x**3 - x**2 - 1
fPrime = lambda x: 3*x**2 -2*x
estimate = newton(f, fPrime, 1, 1e-10, 10)
print("estimate = ", estimate)

print("\n sample 6")

f = lambda x: x**(1/3)
fPrime = lambda x: 1/(3*x**(2/3))
estimate = newton(f, fPrime, 0.1, 1e-2, 10)
print("estimate = ", estimate)


# este pedazo de codigo fue el inicio de la clase
# donde aprendimos a derivar con python
# Actividad 3 (del punto extra) se enviara
# o envio archivo con nombre de:
# autoDiff
# Diferenciacion automatica

import sympy as sp
from sympy.abc import x
from sympy import lambdify

print("\n\nSample 1")

fString = "x**2 - 2"
f = lambdify(x, fString)
fPrime = sp.diff(fString, x)
print(fPrime)

print("sample 2")

f = "x**3 + 4*x**2 - 10"
fPrime = sp.diff(f, x)
print(fPrime)

print("sample 3")
f = "sqrt(x) - cos(x)"
fPrime = sp.diff(f, x)
print(fPrime)

print("sample 4")
f = "x**2 - 10*cos(x)"
fPrime = sp.diff(f, x)
print(fPrime)

print("sample 5")
f = "x**3 - x**2 - 1"
fPrime = sp.diff(f, x)
print(fPrime)

print("sample 6")
f = "x**(1/3)"
fPrime = sp.diff(f, x)
print(fPrime)
