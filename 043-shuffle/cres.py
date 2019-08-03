# Day 43: Shuffle

import random

def shuffle(lst):
    length = len(lst)
    for i in range(length):
        x = random.randint(i, length-1)
        lst[i], lst[x] = lst[x], lst[i]
    return lst


print(shuffle([1,6,4,2,7,2,5,8,9,2,3,4,8,2]))

# result:
# [8, 2, 7, 3, 9, 4, 2, 5, 2, 6, 2, 1, 4, 8]
# [4, 2, 9, 1, 7, 5, 3, 4, 6, 8, 2, 2, 2, 8]
# [1, 6, 9, 2, 2, 4, 3, 7, 8, 2, 4, 2, 5, 8]
