# Day 11 McCarthy 91

def mccarthy(n):
    if n > 100:
        return n - 10
    else:
        return mccarthy(mccarthy(n + 11))

print(mccarthy(6))
