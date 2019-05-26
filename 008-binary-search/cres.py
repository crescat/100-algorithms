# Day 8: Binary search on sorted array

def search(array, item, cursor):
    if len(array) == 1:
        if array[0] == item:
            return cursor
        return False

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    if item < left[-1]:
        return search(left, item, middle-1)
    elif item >= right[0]:
        return search(right, item, middle)
