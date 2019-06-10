# Day 22: Determinant

def determinant(mtx):
    if not is_valid(mtx):
        raise Exception('Matrix should be NxN')

    n = len(mtx)

    if n == 1:
        return mtx[0][0]
    if n == 2:
        return mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0]

    pivot = mtx[0]
    new_pivot = [-pivot[i] if i%2==1 else pivot[i] for i in range(n)]
    rest = mtx[1:]
    return sum(new_pivot[i]*determinant(remove_col(rest, i)) for i in range(n))


def is_valid(mtx):
    for col in mtx:
        if len(col) != len(mtx):
            return False
    return True


def remove_col(mtx, col):
    return [row[:col]+row[col+1:] for row in mtx]


mtx = [[2, 5, 3, 5],
       [4 ,6, 6, 3],
       [11, 3, 2, -2],
       [4, -7, 9, 3]]

print(determinant(mtx))
