# Day 51: Rabin-Miller

import random

def rabin_miller(n, k):
    if n <= 3:
        return n in [2, 3]
    if n % 2 == 0:
        return False

    # obtain s and d where 2**s * d = n - 1
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d / 2
        s += 1

    # test for k times
    composite = []
    for _ in range(k):
        # get a random number in range [0, n-1]
        a = random.randint(1, n-1)
        cases = []
        for i in range(s):
            result = a ** (2 ** i * d) % n
            if result != 1 and result != n - 1:
                cases.append(False)
            else:
                cases.append(True)
        composite.append(all(cases))

    return composite


print(rabin_miller(97, 10))
