# Day 1: Hanoi Tower
def hanoi(n, left='left', middle='middle', right='right'):
    if n > 0:
        hanoi(n-1, left, right, middle)
        print(left, 'to', right)
        hanoi(n-1, middle, left, right)
