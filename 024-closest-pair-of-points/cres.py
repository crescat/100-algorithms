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


def search(lst_of_points):
    points = sorted(lst_of_points)

    def search_helper(points):
        if len(points) <= 1:
            return float('inf'), None, None
        if len(points) == 2:
            return dist(points[0], points[1]), points[0], points[1]

        m = len(points) // 2
        left = points[:m]
        right = points[m:]
        middle_x = points[m][0]

        min_left = search_helper(left)
        min_right = search_helper(right)
        min_lr = min(min_left, min_right, key=lambda x: x[0])
        cross_l, cross_r = [], []

        for x, y in points:
            diff = x - middle_x
            if diff < 0 and diff >= -min_lr[0]:
                cross_l.append((x, y))
            if diff >= 0 and diff <= min_lr[0]:
                cross_r.append((x, y))

        cross_dist = [(dist(a, b), a, b) for a in left for b in right]
        min_cross = min(cross_dist, key=lambda x: x[0])

        return min(min_lr, min_cross, key=lambda x: x[0])

    return search_helper(points)


from random import randint
from PIL import Image, ImageDraw

im = Image.new('RGB', (800, 600), color=(255,255,255))
draw = ImageDraw.Draw(im)

lst = [(randint(0, 800), randint(0, 600)) for _ in range(100)]
r = 2

min_dist, a, b = search(lst)
print(min_dist, a, b)

for x, y in lst:
    box = [(x-r, y-r), (x+r, y+r)]
    if (x, y) == a or (x, y) == b:
        draw.ellipse(box, fill = (255, 0, 0), outline = (255, 0, 0))
    else:
        draw.ellipse(box, fill = (0, 0, 0), outline = (0, 0, 0))

draw.line([a, b], fill=(0,0,0), width = 1)

im.show()
