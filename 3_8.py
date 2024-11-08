'''3 уровень
8. В матрице размером 7 × 5 переставить строки таким образом, чтобы количества положительных элементов в строках следовали в
порядке убывания.'''


def f(x):

    for i in range(7):
        c = 0
        for j in range(5):
            if x[i][j] > 0: c += 1
        x[i] += [c]
    x.sort(key=lambda x: x[5])
    arr = []
    for i in range(6, -1, -1):
        arr += [x[i][:5]]
    return arr
from random import *
matrix = [[randint(-10, 10) for _ in range(5)] for _ in range(7)]
print(*matrix)
print(*f(matrix))
