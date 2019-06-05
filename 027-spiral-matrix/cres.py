# Day 27: Spiral matrix

def spiral(n):
    mtx = [[0] * n for _ in range(n)]
    lst = list(range(1,n*n+1))
    i = 0
    while len(lst) > 0:
        for _ in range(4):
            for j in range(n):
                if mtx[i][j] == 0:
                    mtx[i][j] = lst.pop(0)
            mtx = rotate_ccw(mtx)
        i += 1
    return mtx


def rotate_ccw(mtx):
    return [list(x) for x in zip(*mtx)][::-1]


def print_mtx(mtx):
    for row in mtx:
        print(row)


print_mtx(spiral(6))
