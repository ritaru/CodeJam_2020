import numpy as np
from collections import deque

def check_repeated_items(matrix):
    count = 0
    for row in matrix:
        if len(set(row)) < len(row):
            count = count + 1

    return count


def count_diagonal_sum(matrix):
    diagonalSum = 0

    try:
        for item in matrix.tolist():
            diagonalSum = diagonalSum + item
    except TypeError:
        print('The input type is not np.ndarray')

    return diagonalSum


def solution(testSize):
    k = []
    r = []
    c = []
    
    for i in range(testSize):
        matrixSize = int(input())
        matrix = []

        for t in range(matrixSize):
            matrix.append(list(map(lambda x: int(x), input().split())))
        
        matrix = np.array(matrix)
        k.append(count_diagonal_sum(matrix.diagonal()))
        r.append(check_repeated_items(matrix.tolist()))
        c.append(check_repeated_items(matrix.transpose().tolist()))

    return [k, r, c]


if __name__ == '__main__':
    testSize = int(input())
    values = solution(testSize)
    
    for i in range(testSize):
        print('Case #{}: {} {} {}'.format(i + 1, values[0][i], values[1][i], values[2][i]))