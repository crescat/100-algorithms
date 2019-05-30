import random

def karatsuba_mult(a, b):
    binary_a = bin(a)[::-1]
    result = 0
    for i in range(len(binary_a)):
        if binary_a[i] == '1':
            result += b * 2 ** i
    return result


def naive_mult(a, b):
    x, y = str(a), str(b)
    result = 0

    lst = [[int(i) * int(j) for j in y[::-1]] for i in x[::-1]]

    for m in range(len(lst)):
        for n in range(len(lst[0])):
            result += lst[m][n] * 10 ** (m + n)

    return result

N = 500
A = int(''.join([str(random.randint(0, 9)) for _ in range(N)]))
B = int(''.join([str(random.randint(0, 9)) for _ in range(N)]))

import cProfile
cProfile.run('karatsuba_mult(A, B)')
cProfile.run('naive_mult(A, B)')
cProfile.run('A * B')
