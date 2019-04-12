import numpy as np
np.set_printoptions(linewidth=20000);


# this function takes an augmented matrix and converts it to reduced
# echlon form
def to_reduced_echlon(aug):
    rows = np.size(aug, 0)
    cols = np.size(aug, 1) - 1

    i = 0;
    j = 0;
    counter = 1;

    while (i < rows) & (j < cols):

        k = i
        while aug[k, j] == 0:
            k += 1
            if k >= rows:
                break

        if k >= rows:
            j += 1
            continue

        if (k < rows) & (k != i):
            aug[[i, k]] = aug[[k, i]]

        aug[i] = np.divide(aug[i], aug[i, j])

        for r in range(0, rows):
            if r == i:
                continue
            temp1 = aug[r, j] / aug[i, j]
            temp1 *= -1
            temp2 = np.add(temp1 * aug[i], aug[r])
            aug[r] = temp2
        i += 1
        j += 1

        print("Step " + str(counter))
        print(aug)
        print()
        counter += 1


n = int(input("enter n : "))

A = np.arange(n * n * 1.0).reshape(n, n)
b = np.arange(n * 1.0).reshape(n, 1)
x = [0 for i in range(n)]

print("enter matrix A")
for i in range(n):
    row = input()
    k = 0
    for j in row.split(" "):
        A[i][k] = float(j)
        k += 1

print("enter vector b")
for i in range(n):
    b[i] = float(input())

A = np.hstack((A, b))


print("**********************")
print(A)
print("**********************")
print("Converting to reduced echlon form ...")
print()
to_reduced_echlon(A)

for i in range(n):
    x[i] = "any value"

i = n - 1
j = n - 1
flag = True
while i >= 0 & j >= 0:
    if A[i][j] == 1:
        x[j] = A[i][n]
        i -= 1
        j -= 1
    elif A[i][n] != 0:
        flag = False
        i -= 1

if not flag:
    for i in range(n):
        x[i] = "no value"

print("**********************")
print("This is the answer matrix")
print(x)
