# Day 13: Extended euclidean algorithm

def gcd(x, y):
    a, b = x, y
    while True:
        if a > b:
            a -= b
        elif a < b:
            b -= a
        else:
            return a


print(gcd(252, 105))
