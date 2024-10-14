import numpy as np

def refactorDeterminant(A, file, eqName):
    determinant = calculateDeterminant(A, file, eqName)
       
    if determinant is None:
        file.write(f"\n**The determinant of {eqName} is not defined, the system may not be solvable.**\n")
    elif np.isclose(determinant, 0):
      file.write("\n**The determinant is 0, checking for special cases (infinite/no solutions).**\n")
        

def calculateDeterminant(A, file, eqName):
    try:
        determinant = np.linalg.det(A)
        file.write(f"\n#### Determinant of Matrix {eqName}:\n")
        file.write(f"```\n{determinant}\n```\n")
        return determinant
    except np.linalg.LinAlgError:  # Handle cases where determinant is not defined
        file.write(f"\n#### Determinant of Matrix {eqName}: Not possible\n")
        return None

def solvePunkte(name, A, B, resolvable, file):
    if resolvable == 0:
        C = np.concatenate((A, B), axis=1)
        file.write(f"# System: {name} is not a linear system equation\n")
        file.write(f"```\n{C}\n```\n")
        file.write(f"### A matrix is possible to write but the exponent of any of the variables is wrong\n")
    else:
        file.write(f"# System: {name} (it's linear)\n")
        printMatrixInfo(name, A, B, file)

        refactorDeterminant(A, file, "A")
        refactorDeterminant(B, file, "B")
        
        # Calculate determinant of A
                # Proceed to Gauss-Jordan elimination and classification
        result, scenario = gj(A, B, file)

        file.write("\n#### Final Escalonated Matrix (RREF):\n")
        file.write(f"```\n{result}\n```\n")
        
        # Based on the scenario, classify the system
        if scenario == "no_solution":
            file.write("\n### Conclusion: The system has **no solution** due to an inconsistency (e.g., `0 = 1`).\n")
        elif scenario == "infinite_solutions":
            file.write("\n### Conclusion: The system has **infinite solutions**.\n")
        else:
            file.write("\n### Conclusion: The system has **one unique solution**.\n")
            file.write("\n#### Solution x:\n")
            x = result[:, -1]
            file.write(f"```\n{x}\n```\n")

def printMatrixInfo(name, A, B, file):
    C = np.concatenate((A, B), axis=1)
    file.write(f"\n**System: {name}**\n")
    file.write(f"```\n{C}\n```\n")
    file.write(f"Size of {name}: {np.shape(C)}\n")
    file.write("Matrix Equation: Ax = b\n")
    printMatrixNotation(A, B, file)


def gj(A ,B, file):
    C = np.concatenate((A, B), axis=1)
    rows, cols = C.shape
    file.write("\n#### Augmented Matrix:\n")
    file.write(f"```\n{C}\n```\n")
    
    for j in range(min(rows, cols - 1)):
        # Find pivot
        pivot_row = j
        for i in range(j, rows):
            if abs(C[i, j]) > abs(C[pivot_row, j]):
                pivot_row = i
        
        # Swap rows if necessary
        if pivot_row != j:
            C[[j, pivot_row]] = C[[pivot_row, j]]
            file.write(f"\n### Swapped row {j} with row {pivot_row}\n")
        
        # Check if pivot is too small
        if abs(C[j, j]) < 1e-10:
            file.write(f"\n### Small pivot encountered in column {j}, skipping.\n")
            continue
        
        # Normalize the pivot row
        C[j] = C[j] / C[j, j]
        
        # Eliminate in other rows
        for i in range(rows):
            if i != j:
                C[i] = C[i] - C[i, j] * C[j]
    
    # Check for inconsistent or dependent rows
    rank = np.linalg.matrix_rank(C[:, :-1])
    aug_rank = np.linalg.matrix_rank(C)
    
    if rank < aug_rank:
        file.write("\n**Inconsistent system detected**\n")
        return C, "no_solution"
    elif rank < cols - 1:
        file.write("\n**Dependent equations detected**\n")
        return C, "infinite_solutions"
    else:
        return C, "one_solution"

def printMatrixNotation(A, B, file):
    rows, cols = A.shape
    x_variables = [f"x{i+1}" for i in range(cols)]
    
    file.write("\n#### Matrix Notation Ax = b:\n")
    for i in range(rows):
        row_str = " + ".join([f"{A[i,j]:.2f}{x_variables[j]}" for j in range(cols) if A[i,j] != 0])
        file.write(f"{row_str} = {B[i][0]:.2f}\n")

def solveMultipleSystems(systems, file):
    for name, (A, B, resolvable) in systems.items():
        solvePunkte(name, A, B, resolvable, file)



