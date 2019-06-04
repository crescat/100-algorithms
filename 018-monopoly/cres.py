# Day 18: Monopoly

def probability(n):
    if n <= 0:
        return 0
    if n <= 6:
        return 1/6 + sum(probability(n - i) for i in range(1, 7)) / 6
    return sum(probability(n - i) for i in range(1, 7)) / 6

print(probability(10))
