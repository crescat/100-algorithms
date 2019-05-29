# Day 13: Extended euclidean algorithm

def gcd(x, y):
    while True:
        if b == 0:
            return x
        else:
            c = a % b
            a, b = b, c

def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extended_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, g


print(extended_gcd(56, 252))
