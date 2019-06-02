def merge_sort(lst):
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

    left, lcount = merge_sort(lst[:m])
    right, rcount = merge_sort(lst[m:])
    result, count = merge(left, right)
    return result, lcount + rcount + count


def naive_inversions(lst):
    count = 0
    for i in range(len(lst)):
        pivot = lst[i]
        rest = lst[i+1:]
        count += len([rest[j] for j in range(len(rest)) if pivot > rest[j]])
    return count


print(naive_inversions([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))
