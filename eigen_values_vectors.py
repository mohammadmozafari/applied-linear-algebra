import numpy as np
import numpy.random as rnd
import numpy.linalg as la

np.set_printoptions(linewidth=300)


def power_method(a, k):
    n = np.size(a, 1)
    if n <= 20 or k < 0:
        print('wrong arguments :(')
        return
    x = rnd.rand(n, 1)
    x[5, 0] = 1
    x[10, 0] = 1
    for i in range(k):
        x = x / np.amax(x)
        x = a @ x
    return np.amax(x), x


def inverse_power_method(a, k):
    n = np.size(a, 1)
    if n <= 20 or k < 0:
        print('wrong arguments :(')
        return
    mu = 130
    x = rnd.rand(n, 1)
    x[5, 0] = 1
    x[10, 0] = 1
    for i in range(k):
        coe = a - mu * np.eye(n)
        y = la.solve(coe, x[:, 0])
        s = np.amax(y)
        v = mu + 1 / s
        x[:, 0] = y / s
    return v, x


def estimate(y):
    m = np.size(y, 0)
    x = np.ones([m, 1])
    x = np.hstack((x, np.array(range(m)).reshape([m, 1])))
    x = np.hstack((x, x[:, 1:2] ** 2))
    coe = x.T @ x
    b = x.T @ y
    theta = la.solve(coe, b)
    return theta


def main():
    a = rnd.rand(21, 21)
    a = a * 10
    print('A : ')
    print(a.round(2))
    print()
    print('e-value with numpy library : ')
    eig = la.eig(a)
    maxIndex = np.where(eig[0] == np.amax(eig[0]))[0]
    print(eig[0][maxIndex].round(2))
    print('---------------------------------')
    print('estimated e-value and e-vector with power method : ')
    x, y = power_method(a, 50)
    print(x.round(2))
    print(y.round(2))
    print('checking answer : Ax - Lx must be near 0')
    print((a @ y - x * y).round(2))
    print('---------------------------------')
    print('estimated e-value and e-vector with inveres power method : ')
    x, y = inverse_power_method(a, 50)
    print(x.round(2))
    print(y.round(2))
    print('checking answer : Ax - Lx must be near 0')
    print((a @ y - x * y).round(2))
    print('\n*********************************\n*********************************')
    y = np.array([[0],
                  [8.8],
                  [9.29],
                  [63],
                  [104.7],
                  [159.1],
                  [222.0],
                  [294.5],
                  [380.4],
                  [471.1],
                  [571.7],
                  [686.8],
                  [809.2]])
    print('least square answer : ')
    coe = estimate(y)
    print(coe.round(2))
    print('estimated speed at t = 4.5')
    t = np.array([[4.5],[9]])
    print((coe[1:, :].T @ t).round(2))


main()
