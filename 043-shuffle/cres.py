# Day 43: Shuffle

import random

def shuffle(lst):
    length = len(lst)
    for i in range(length):
        x = random.randint(i, length-1)
        lst[i], lst[x] = lst[x], lst[i]
    return lst


print(shuffle([3,6,4,2,7,2,5,8,9,2,3,4,8,2]))

# result:
# [2, 9, 5, 4, 2, 4, 6, 3, 2, 2, 3, 8, 8, 7]
# [8, 9, 7, 3, 2, 6, 5, 4, 2, 2, 3, 4, 2, 8]
# [5, 8, 4, 4, 8, 6, 3, 2, 3, 2, 2, 2, 7, 9]
