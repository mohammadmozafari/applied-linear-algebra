import numpy as np
from fractions import Fraction as fr

np.set_printoptions(linewidth=20000);

def lu_factor(A):
    [n, n1] = np.shape(A)
    if n != n1:
        print("Error: Squared matrix needed")
    L = np.eye(n, n, 0, fr)
    U = np.zeros([n, n], fr)

    for i in range(n):
        for j in range(i, n):
            temp = fr(0)
            for k in range(i):
                temp += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - temp
        for j in range(i + 1, n):
            temp = fr(0)
            for k in range(i): 
                temp += L[j, k] * U[k, i]
            L[j, i] = A[j, i] - temp
            L[j, i] = L[j, i] / U[i, i]

    return [L, U]

def forward_substitution(L, b):
    n = np.shape(b)[0]
    y = np.zeros([n, 1], fr)
    for i in range(n):
        temp = 0
        for j in range(i):
            temp += L[i, j] * y[j, 0]
        y[i, 0] = fr(b[i, 0] - temp)
    return y

def backward_substitution(U, y):
    n = np.shape(y)[0]
    x = np.zeros([n, 1], fr)
    for i in reversed(range(n)):
        temp = 0
        for j in reversed(range(i + 1, n)):
            temp += U[i, j] * x[j, 0]
        x[i, 0] = fr(y[i, 0] - temp) / fr(U[i, i])
    return x

def linear_sys_solver(A, b):
    [L, U] = lu_factor(A)
    return (backward_substitution(U, forward_substitution(L, b)))

def myinverse(A):
    n = np.shape(A)[0]
    X = np.zeros([n, n], A.dtype)
    I = np.eye(n, n, 0, A.dtype)
    [L, U] = lu_factor(A)

    for i in range(n):
        y = forward_substitution(L, I[0:n, i:i+1])
        x = backward_substitution(U, y)
        X[0:n, i:i+1] = x[0:n, 0:1]; 

    return X

def printFractionMatrix(M):
    n = np.shape(M)[0];
    print("[");
    if M.dtype == float:
        for i in range(n):
            print(" ", end = " ")
            for j in range(n):
                print(round(M[i, j]), end = "     ")
            print()
    else:
        for i in range(n):
            print(" ", end = " ")
            for j in range(n):
                print(M[i, j], end = "     ")
            print()
    print("]")

def hilbert(n):
    hilber_fr = np.ones([n, n], fr)
    for i in range(n):
        for j in range(n):
            hilber_fr[i, j] = 1 / fr(i + j + 1)
    
    hilbert_float = np.ones([n, n], float)
    for i in range(n):
        for j in range(n):
            hilbert_float[i, j] = 1 / (i + j + 1)
    
    print("H * myinverse(H): ")
    printFractionMatrix(np.dot(hilber_fr, myinverse(hilber_fr)))
    print("H * inv(H): ")
    hinv = np.linalg.inv(hilbert_float)
    printFractionMatrix(np.dot(hilbert_float, hinv))


A = np.array([[3, -7, -2, 2],
              [-3, 5, 1, 0],
              [6, -4, 0, -5],
              [-9, 5, -5, 12]], fr)

b = np.array([[2],
              [5],
              [7]], fr)

#The following are the different parts of the exercise, uncomment the part you want to test.

#print("*************** LU FACTORS ***************")
#[L, U] = lu_factor(A)
#print("L = ")
#printFractionMatrix(L)
#print("U = ")
#printFractionMatrix(U)

#print("*************** SOLVE EQUATION ***************")
#print("Equation: \n", np.hstack([A, b]))
#x = linear_sys_solver(A, b)
#printFractionMatrix(x)

#print("*************** COMPUTING INVERSE ***************")
#Ainv = myinverse(A)
#print("A inverse:")
#printFractionMatrix(Ainv)

#print("*************** HILBERT ***************")
#print("Hilbert 5")
#hilbert(5)
#print()
#print("Hilbert 10")
#hilbert(10)
#print()
#print("Hilbert 15")
#hilbert(15)
#print()
#print("Hilbert 20")
#hilbert(20)
#print()