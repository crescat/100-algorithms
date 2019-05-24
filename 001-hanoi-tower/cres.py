# Day 1: Hanoi Tower
def hanoi(n, source = 1, target = 3, spare = 2):
    if n < 0:
        return 'Invalid input!'
    
    if n == 0:
        return []

    if n > 0:
        return \
            hanoi(n - 1, source, spare, target) + \
            [move(source, target)] + \
            hanoi(n - 1, spare, target, source)
        

def move(a, b):
    return (a, b)


def check_hanoi(n, sequence):
    board = [n, 0, 0]
    for a, b in sequence:
        board[a-1] -= 1
        board[b-1] += 1
    return board

n = 5

print(hanoi(n))
print(check_hanoi(n, hanoi(n)))