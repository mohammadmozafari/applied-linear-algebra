import numpy as np


def to_reduced_echlon(matrix):
    a = np.copy(matrix)
    rows = np.size(a, 0)
    cols = np.size(a, 1)

    i = 0
    j = 0

    while (i < rows) & (j < cols):

        k = i
        while a[k, j] == 0:
            k += 1
            if k >= rows:
                break

        if k >= rows:
            j += 1
            continue

        if (k < rows) & (k != i):
            a[[i, k]] = a[[k, i]]

        a[i] = np.divide(a[i], a[i, j])

        for r in range(0, rows):
            if r == i:
                continue
            temp1 = a[r, j] / a[i, j]
            temp1 *= -1
            temp2 = np.add(temp1 * a[i], a[r])
            a[r] = temp2

        i += 1
        j += 1

    return a


def find_null_base(matrix):
    e = to_reduced_echlon(matrix)
    rows = np.size(e, 0)
    cols = np.size(e, 1)

    # find free variables
    free_cols = []
    i = j = 0
    while j < cols:
        if (i < rows - 1) & (e[i, j] == 1):
            i += 1
            j += 1
        elif e[i, j] == 1:
            j += 1
        else:
            free_cols.append(j)
            j += 1

    # set one for free variables
    base = np.zeros([cols, len(free_cols)])
    index = 0
    for item in free_cols:
        base[item, index] = 1
        index += 1
    i = 0

    # setting other elements of basis
    while i < rows:
        k = 0
        while k < cols:
            if e[i, k] == 1:
                break
            k += 1
        if k == cols:
            break

        index = 0
        for item in free_cols:
            base[k, index] = -1 * e[i, item]
            index += 1
        i += 1

    return base


def find_col_base(matrix):
    e = to_reduced_echlon(matrix)
    rows = np.size(e, 0)
    cols = np.size(e, 1)

    # find basic variables
    basic_cols = []
    i = j = 0
    while j < cols:
        if (i < rows - 1) & (e[i, j] == 1):
            basic_cols.append(j)
            i += 1
            j += 1
        elif e[i, j] == 1:
            basic_cols.append(j)
            break
        else:
            j += 1

    # find free variables
    free_cols = []
    j = 0
    while j < cols:
        if j not in basic_cols:
            free_cols.append(j)
        j += 1

    # finding the basis
    base = matrix[:, basic_cols]

    # find other columns by basis
    coe = np.zeros([len(basic_cols), len(free_cols)])
    ind = 0
    for item in free_cols:
        print(np.hstack((base, matrix[:, item:item + 1])))
        echlon = to_reduced_echlon(np.hstack((base, matrix[:, item:item + 1])))
        coe[:, ind] = echlon[:len(basic_cols), np.size(echlon, 1) - 1]
        ind += 1

    return base, coe, free_cols


def find_row_base(matrix):
    e = to_reduced_echlon(matrix)
    rows = np.size(e, 0)
    cols = np.size(e, 1)

    zero_help = np.zeros([1, cols])
    i = rows - 1
    while i >= 0:
        if not np.array_equal(zero_help[0, :], e[i, :]):
            break
        i -= 1

    return e[0:i + 1, :]


def test_controllable(a, b):
    n = np.size(a, 0)
    matrix = b
    product = np.matmul(a, b)
    for i in range(n - 1):
        matrix = np.hstack((matrix, product))
        product = np.matmul(a, product)

    return np.size(find_row_base(matrix), 0) == n


def get_matrix():
    rows = int(input('Enter the number of rows : '))
    cols = int(input('Enter the number of columns : '))

    elements = list(map(float, input('Enter the entries in a single line separated by space : ').split(' ')))
    matrix = np.array(elements, float).reshape(rows, cols)
    return matrix


def main():
    print('-----------------------------------------------------------')
    print('Finding the basis of null space, row space and column space')
    print('-----------------------------------------------------------')

    a = get_matrix()
    print()
    print(a)
    print()

    print('The columns of the following matrix are a basis for null space :')
    print(find_null_base(a))
    print()
    print('****************************')
    print('****************************')
    print()

    print('The rows of the following matrix are a basis for row space')
    print(find_row_base(a))
    print()
    print('****************************')
    print('****************************')
    print()

    (basis, coe, free) = find_col_base(a)
    print('The columns of the following matrix are a basis for column space')
    print(basis)
    print()
    print('Building other columns by the basis : ')
    print('The vectors are the coefficients of the basis vectors constructing other columns')

    index = 0
    for item in free:
        print('column ', item, ' :')
        print(coe[:, index])
        print()
        index += 1

    print()
    print('****************************')
    print('****************************')
    print()

    print('-----------------------------------------------------------')
    print('Checking whether a pair of matrices are controllable or not')
    print('-----------------------------------------------------------')

    print('Enter A : ')
    a = get_matrix()
    print('Enter B : ')
    b = get_matrix()

    print('\nA = ')
    print(a, '\n')
    print('\nB = ')
    print(b, '\n')

    print('Controllable : ', test_controllable(a, b))


# Start the execution of program
main()
