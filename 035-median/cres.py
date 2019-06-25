# Day 35: Median
import random

def find_nth(lst, n):
    if len(set(lst)) == 1:
        return lst[0]

    pivot = lst[random.randint(0, len(lst)-1)]
    left = [x for x in lst if x <= pivot]
    right = [x for x in lst if x > pivot]

    if len(left) > n:
        return find_nth(left, n)
    else:
        return find_nth(right, n-len(left))


lst = [5,8,6,3,2,4,87,9,6,3,2,1,1,2,88,7,4,2,6,9,8,5]

print(find_nth(lst, 2))
