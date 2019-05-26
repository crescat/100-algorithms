# Day 9: Monte carlo - pi

from random import uniform

def calc_pi(n):
    random_nums = [(uniform(-1, 1), uniform(-1, 1)) for _ in range(n)]
    count = 0
    for x, y in random_nums:
        if x*x + y*y <= 1:
            count += 1
    return float(count) / float(n) * 4

print(calc_pi(1000000))
