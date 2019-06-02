def inversions(lst):
    def merge(lst1, lst2):
        if lst1 == []:
            return lst2, 0

        if lst2 == []:
            return lst1, 0

        if lst1[0] >= lst2[0]:
            merged, count = merge(lst1, lst2[1:])
            return [lst2[0]] + merged, count+1

        if lst1[0] < lst2[0]:
            merged, count = merge(lst1[1:], lst2)
            return [lst1[0]] + merged, count

    if lst == []:
        return [], 0

    if len(lst) == 1:
        return lst, 0

    m = len(lst) // 2

    left, lcount = inversions(lst[:m])
    right, rcount = inversions(lst[m:])
    result, count = merge(left, right)
    return result, lcount+rcount

print(inversions([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))
