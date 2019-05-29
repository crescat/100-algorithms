# Day 13: Extended euclidean algorithm

def gcd(x, y):
    a, b = x, y
    while True:
        if a == 0 or b == 0:
            return max(a, b)
        if a > b:
            a %= b
        else:
            b %= a


print(gcd(252, 14))
