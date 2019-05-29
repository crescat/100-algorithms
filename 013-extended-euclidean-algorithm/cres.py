# Day 13: Extended euclidean algorithm

def gcd(x, y):
    while True:
        if y == 0:
            return x
        else:
            z = x % y
            x, y = y, z





print(gcd(28, 252))
