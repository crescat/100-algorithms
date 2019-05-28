# Day 11 McCarthy 91

def mccarthy(n):
    if n > 100:
        return n - 10
    else:
        return mccarthy(mccarthy(n + 11))

print(mccarthy(6))

def n_mccarthy(n, x):
    if n > x:
        return n - 10
    else:
        return n_mccarthy(n_mccarthy(n + 11, x), x)

for x in range(1, 100):
    print(n_mccarthy(50, x))
