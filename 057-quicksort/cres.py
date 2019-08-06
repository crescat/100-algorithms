# Day 57: Quicksort
import random

def _sort(data, low, high):
    pivot = data[high]
    i = low
    for j in range(low, high):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return i


def sort(data, low, high):
    if low < high:
        i = _sort(data, low, high)

        sort(data, low, i-1)
        sort(data, i+1, high)


data = [3,5,6,2,3,5,6,99,8,7,66,4,2,2,2,11,0,5]
print(data)
sort(data, 0, len(data)-1)
print(data)

# result:
# [0, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 11, 66, 99]
