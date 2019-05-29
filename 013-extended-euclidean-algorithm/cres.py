# Day 13: Extended euclidean algorithm

def gcd(x, y):
    a, b = max(x, y), min(x, y)
    while True:
        if b == 0:
            return a
        else:
            c = a % b
            a, b = b, c


print(gcd(252, 28))
