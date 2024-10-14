# Erick Gonzalez Parada | Partial Exam II | 178145
## Solving the Matrix Systems

# System: exe1 (it's solvable)

**System: exe1**
```
[[ 1. -2.  3. 11.]
 [ 4.  1. -1.  4.]
 [ 2. -1.  3. 10.]]
```
Size of exe1: (3, 4)
Matrix Equation: Ax = b

#### Matrix Notation Ax = b:
1.00x1 + -2.00x2 + 3.00x3 = 11.00
4.00x1 + 1.00x2 + -1.00x3 = 4.00
2.00x1 + -1.00x2 + 3.00x3 = 10.00

#### Determinant of Matrix A:
```
11.999999999999995
```

#### Determinant of Matrix B: Not possible

**The determinant of B is not defined, the system may not be solvable.**

#### Augmented Matrix:
```
[[ 1. -2.  3. 11.]
 [ 4.  1. -1.  4.]
 [ 2. -1.  3. 10.]]
```

### Swapped row 0 with row 1

#### Final Escalonated Matrix (RREF):
```
[[ 1.  0.  0.  2.]
 [ 0.  1.  0. -3.]
 [ 0.  0.  1.  1.]]
```

### Conclusion: The system has **one unique solution**.

#### Solution x:
```
[ 2. -3.  1.]
```
# System: exe2 (it's solvable)

**System: exe2**
```
[[ 0.  9. -7.  2.]
 [ 0.  0. -1. -2.]
 [-3.  6.  8.  1.]]
```
Size of exe2: (3, 4)
Matrix Equation: Ax = b

#### Matrix Notation Ax = b:
9.00x2 + -7.00x3 = 2.00
-1.00x3 = -2.00
-3.00x1 + 6.00x2 + 8.00x3 = 1.00

#### Determinant of Matrix A:
```
27.0
```

#### Determinant of Matrix B: Not possible

**The determinant of B is not defined, the system may not be solvable.**

#### Augmented Matrix:
```
[[ 0.  9. -7.  2.]
 [ 0.  0. -1. -2.]
 [-3.  6.  8.  1.]]
```

### Swapped row 0 with row 2

### Swapped row 1 with row 2

#### Final Escalonated Matrix (RREF):
```
[[ 1.          0.          0.          8.55555556]
 [ 0.          1.          0.          1.77777778]
 [-0.         -0.          1.          2.        ]]
```

### Conclusion: The system has **one unique solution**.

#### Solution x:
```
[8.55555556 1.77777778 2.        ]
```
# System: exe3 (it's solvable)

**System: exe3**
```
[[  1.   2.  -2.  -1.   1.]
 [ -3.   4.   1.  -2.   4.]
 [ -3.  14.  -4.  -7.   3.]
 [  6.  12. -12.  -6.   5.]]
```
Size of exe3: (4, 5)
Matrix Equation: Ax = b

#### Matrix Notation Ax = b:
1.00x1 + 2.00x2 + -2.00x3 + -1.00x4 = 1.00
-3.00x1 + 4.00x2 + 1.00x3 + -2.00x4 = 4.00
-3.00x1 + 14.00x2 + -4.00x3 + -7.00x4 = 3.00
6.00x1 + 12.00x2 + -12.00x3 + -6.00x4 = 5.00

#### Determinant of Matrix A:
```
0.0
```

**The determinant is 0, checking for special cases (infinite/no solutions).**

#### Determinant of Matrix B: Not possible

**The determinant of B is not defined, the system may not be solvable.**

#### Augmented Matrix:
```
[[  1.   2.  -2.  -1.   1.]
 [ -3.   4.   1.  -2.   4.]
 [ -3.  14.  -4.  -7.   3.]
 [  6.  12. -12.  -6.   5.]]
```

### Swapped row 0 with row 3

### Swapped row 1 with row 2

### Small pivot encountered in column 2, skipping.

### Small pivot encountered in column 3, skipping.

**Inconsistent system detected**

#### Final Escalonated Matrix (RREF):
```
[[ 1.          0.         -1.          0.          0.28333333]
 [ 0.          1.         -0.5        -0.5         0.275     ]
 [ 0.          0.          0.          0.          3.75      ]
 [ 0.          0.          0.          0.          0.16666667]]
```

### Conclusion: The system has **no solution** due to an inconsistency (e.g., `0 = 1`).
