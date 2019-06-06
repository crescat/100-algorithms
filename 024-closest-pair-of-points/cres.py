# Day 24: Closest pair of points

import math

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def naive_search(lst_of_points):  # O(n^2) time complexity
    num = len(lst_of_points)
    dist_list = []
    for i in range(num-1):
        for j in range(i+1, num):
            x, y = lst_of_points[i], lst_of_points[j]
            dist_list.append((dist(x, y), x, y))
    return min(dist_list)

lst = [(1,2), (5,8), (2,1), (8,3), (0,7)]
print(naive_search(lst))
