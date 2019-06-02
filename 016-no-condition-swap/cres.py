# Day 16: No-condition swap

def swap(a, b):
    return a+b-(min(a, b)), a+b-(max(a,b))

def swap2(a, b):
    avg = (a + b) / 2
    diff = abs(a - b)
    return avg-diff/2, avg+diff/2

print(swap2(99, 62))
