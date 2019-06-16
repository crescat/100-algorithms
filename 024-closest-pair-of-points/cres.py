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
        margin = min(min_left, min_right, key=lambda x: x[0])[0]

        cross_l = [(x, y) for x, y in left  if middle_x - x <= margin]
        cross_r = [(x, y) for x, y in right if x - middle_x <= margin]
        valid_pairs = []

        for x1, y1 in cross_l:
            for x2, y2 in cross_r:
                if x2 - x1 <= margin and abs(y2 - y1) <= margin:
                    valid_pairs.append([(x1, y1), (x2, y2)])

        cross_dist = [(dist(pair[0], pair[1]), pair[0], pair[1]) for pair in valid_pairs]

        if cross_dist != []:
            min_cross = min(cross_dist, key=lambda x: x[0])
        else:
            min_cross = (float('inf'), None, None)

        return min([min_left, min_right, min_cross], key=lambda x: x[0])

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
