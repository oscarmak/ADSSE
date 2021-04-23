import numpy as np
import tracemalloc
import time




# creates random matrix of size n x n
def random_matrices(n):
    m1 = np.random.randint(10, size=(n, n))
    m2 = np.random.randint(10, size=(n, n))
    return m1, m2


# create a matrix filled with 0s
def new_matrix(r, c):
    matrix = np.zeros((r, c))
    return matrix


# splits the matrix n x m
def split(m1):
    n, m = m1.shape

    n = n // 2
    m = m // 2

    a = m1[:n, :m]
    b = m1[:n, m:]
    c = m1[n:, :m]
    d = m1[n:, m:]

    return a, b, c, d


def strassen_multiply(m1, m2):
    n = len(m1)

    # best case: 1x1 matrix
    if n == 1:
        return m1 * m2
    else:
        # splits into quarters
        a, b, c, d = split(m1)
        e, f, g, h = split(m2)

        # p1 = a(f - h)
        p1 = strassen_multiply(a, np.subtract(f, h))

        # p2 = (a + b)h
        p2 = strassen_multiply(np.add(a, b), h)

        # p3 = (c + d)e
        p3 = strassen_multiply(np.add(c, d), e)

        # p4 = d(g - e)
        p4 = strassen_multiply(d, np.subtract(g, e))

        # p5 = (a + d)(e + h)
        p5 = strassen_multiply(np.add(a, d), np.add(e, h))

        # p6 = (b - d)(g + h)
        p6 = strassen_multiply(np.subtract(b, d), np.add(g, h))

        # p7 = (a - c)(e + f)
        p7 = strassen_multiply(np.subtract(a, c), np.add(e, f))

        m3_a = np.add(np.subtract(np.add(p5, p4), p2), p6)
        m3_b = np.add(p1, p2)
        m3_c = np.add(p3, p4)
        m3_d = np.subtract(np.subtract(np.add(p1, p5), p3), p7)

        # submatrices are joined into final matrix
        left_half = np.vstack((m3_a, m3_c))
        right_half = np.vstack((m3_b, m3_d))

        m3 = np.hstack((left_half, right_half))

        return m3


# n = matrix size
n = 1024
m1, m2 = random_matrices(n)

#timing

tracemalloc.start()
start = time.time()

result = strassen_multiply(m1, m2)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

#print(f'Strassen:\n{result}')
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
print(f"Runtime of the program is {end - start} seconds")