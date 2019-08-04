# Day 55: Quincunx
import random
import matplotlib
import matplotlib.pyplot as plot

def update_quincunx(levels, buckets):
    ball_pos = 0
    for _ in range(levels):
        chance = random.randint(0, 1)
        if chance == 0:
            ball_pos -= 0
        else:
            ball_pos += 1
    buckets[ball_pos] += 1
    return buckets

# quincunx level:
level = 20

# bucket:
buckets = [0] * (level + 1)

# put balls in
for _ in range(10000):
    buckets = update_quincunx(level, buckets)

plot.bar(range(-level//2, level//2+1), buckets)
plot.savefig('quincunx.png')
