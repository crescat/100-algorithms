# Day 63: Zig-zag

import random

def zig_zag_index(n):
    mtx = [[None] * n for _ in range(n)]
    value = 0
    x, y = (0, 0)
    current_direction = "right"

    # filling in upper left triangle
    for i in range(0, n*(n+1)//2):
        mtx[x][y] = i
        if current_direction == "left":
            x += 1
            y -= 1
        elif current_direction == "right":
            x -= 1
            y += 1
        if x < 0:
            x = 0
            current_direction = "left"
        if y < 0:
            y = 0
            current_direction = "right"

    # filling in lower right triangle
    for i in range(n):
        for j in range(n):
            if mtx[i][j] == None:
                mtx[i][j] = n * n -1 - mtx[n-1-i][n-1-j]

    return mtx

def matrix_to_zig_zag_values(mtx):
    if not is_square_mtx(mtx):
        return "Matrix should be NxN!"

    n = len(mtx)
    index_mtx = zig_zag_index(n)
    result = [None] * (n*n)

    for i in range(n):
        for j in range(n):
            result[index_mtx[i][j]] = mtx[i][j]

    return result


def zig_zag_values_to_matrix(sequence):
    n = int(len(sequence) ** 0.5)
    if n * n != len(sequence):
        return "Something wrong with sequence length!"

    index_mtx = zig_zag_index(n)
    result = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = sequence[index_mtx[i][j]]

    return result


def print_matrix(mtx):
    for row in mtx:
        print(row)


def is_square_mtx(mtx):
    n = len(mtx)
    for row in mtx:
        if len(row) != n:
            return False
    return True

n = 6

matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
print('Initial matrix:')
print_matrix(matrix)

print('\nAfter processing:')
zig_zag_sequence = matrix_to_zig_zag_values(matrix)
print(zig_zag_sequence)

print('\nRecover matrix:')
new_matrix = zig_zag_values_to_matrix(zig_zag_sequence)
print_matrix(new_matrix)

print('\nIs both matrix the same: {}'.format(matrix == new_matrix))

'''
Result:

Initial matrix:
[3, 0, 7, 1, 1, 7]
[5, 8, 7, 0, 1, 8]
[8, 6, 7, 5, 9, 3]
[4, 2, 3, 8, 8, 2]
[4, 2, 4, 5, 5, 5]
[8, 9, 2, 8, 4, 2]

After processing:
[3, 0, 5, 8, 8, 7, 1, 7, 6, 4, 4, 2, 7, 0, 1, 7, 1, 5, 3, 2, 8, 9, 4, 8, 9, 8, 3, 8, 5, 2, 8, 5, 2, 5, 4, 2]

Recover matrix:
[3, 0, 7, 1, 1, 7]
[5, 8, 7, 0, 1, 8]
[8, 6, 7, 5, 9, 3]
[4, 2, 3, 8, 8, 2]
[4, 2, 4, 5, 5, 5]
[8, 9, 2, 8, 4, 2]

Is both matrix the same: True
'''
