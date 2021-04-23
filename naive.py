import numpy as np
import tracemalloc
import time

#input matrix size n x n
n = int(input('enter matrix size'))

a = np.random.randint(10, size=(n,n))
b = np.random.randint(10, size=(n,n))

def new_m(p, q): # create a matrix filled with 0s
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix

def naive(a, b): # multiply the two matrices
    if len(a[0]) != len(b): # if # of col != # of rows:
        return "Matrices are not m*n and n*p"
    else:
        p_matrix = new_m(len(a), len(b[0]))
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    p_matrix[i][j] += a[i][k]*b[k][j]
    return p_matrix

#timing
start = time.time()
tracemalloc.start()

result = naive(a,b)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()



#print (f'Naive:\n{result}')
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
print(f"Runtime of the program is {end - start} seconds")
