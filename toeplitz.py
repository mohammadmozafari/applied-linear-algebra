import numpy as np
from fractions import Fraction as fr

# this function transforms a matrix to its reduced echlon form
def compute_det(A):
    det = 1
    rows = np.size(A, 0)
    cols = np.size(A, 1)
   
    i = 0;
    j = 0;
    counter = 1;

    while (i < rows) & (j < cols):
        k = i
        while A[k, j] == 0:
            k += 1
            if k >= rows:
                break

        if k >= rows:
            j += 1
            continue

        if (k < rows) & (k != i):
            A[[i, k]] = A[[k, i]]
            det *= -1

        div = A[i, j]
        A[i] = np.divide(A[i], div)
        det *= div

        for r in range(0, rows):
            if r == i:
                continue
            temp1 = A[r, j] / A[i, j]
            temp1 *= -1
            temp2 = np.add(temp1 * A[i], A[r])
            A[r] = temp2
        i += 1
        j += 1

        counter += 1

    zero = False
    for i in range(rows):
        if A[i, i] == 0:
            zero = True
    if zero:
        return 0
    return det

n = int(input("Enter vector size: "))

# taking c vector
print("Enter c")
c = np.zeros(n, fr)
for i in range(n):
    c[i] = fr(eval(input()))

# taking r vector
print("Enter r")
r = np.zeros(n, fr)
for i in range(n):
    r[i] = fr(eval(input()))

# constructing the teoplitz matrix
teo = np.zeros([n, n])
for i in range(n):
    for j in range(n):
        temp = i - j
        if temp < 0:
            teo[i, j] = r[-1*temp]
        else:
            teo[i, j] = c[temp]

# computing determinant
det = compute_det(teo)
print(det)