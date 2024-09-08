#  Actividad 3 
# nombre: Erick Gonzalez Parada
# materia: analisis numerico
# seccion: 1


# Diferenciacion automatica (act 3 separada para mas orden)
import numpy as np
import sympy as sp
from sympy.abc import x
from sympy import lambdify

def newton(f, Df, x0, epsilon, maxIteration):
    if isinstance(f, str):
        f = sp.sympify(f)
    if isinstance(Df, str):
        Df = sp.sympify(Df)
    if not callable(f):
        f = sp.lambdify(x, f)
    if not callable(Df):
        Df = sp.lambdify(x, Df)

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

print("\n\nSample 1")
f = "x**2 - 2"
fPrime = sp.diff(f, x)
print(fPrime)
estimate = newton(f, fPrime, 1.5, 1e-6, 10)
print(estimate)

print("sample 2")
f = "x**3 + 4*x**2 - 10"
fPrime = sp.diff(f, x)
print(fPrime)
estimate = newton(f, fPrime, 1.5, 1e-4, 10)
print(estimate)

print("sample 3")
f = "sqrt(x) - cos(x)"
fPrime = sp.diff(f, x)
print(fPrime)
estimate = newton(f, fPrime, 0.5, 1e-3, 10)
print(estimate)

print("sample 4")
f = "x**2 - 10*cos(x)"
fPrime = sp.diff(f, x)
print(fPrime)
estimate = newton(f, fPrime, -100, 1e-5, 10)
estimate2 = newton(f, fPrime, 50, 1e-5, 10)
print(estimate)
print(estimate2)

print("sample 5")
f = "x**3 - x**2 - 1"
fPrime = sp.diff(f, x)
print(fPrime)
estimate = newton(f, fPrime, 1, 1e-10, 10)
print(estimate)

print("sample 6")
f = "x**(1/3)"
fPrime = sp.diff(f, x)
print(fPrime)
estimate = newton(f, fPrime, 0.1, 1e-2, 10)
print(estimate)
