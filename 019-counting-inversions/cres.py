def merge_sort_inversion(lst):
    if len(lst) == 1:
        return lst, 0

    middle = len(lst) // 2
    left, l_inv = merge_sort_inversion(lst[:middle])
    right, r_inv= merge_sort_inversion(lst[middle:])
    total_inv = l_inv + r_inv

    i, j = 0, 0
    sorted_lst = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_lst += [left[i]]
            i += 1
        else:
            sorted_lst += [right[j]]
            j += 1
            total_inv += (len(left) - i)

    sorted_lst += left[i:]
    sorted_lst += right[j:]

    return sorted_lst, total_inv


def naive_inversions(lst):
    count = 0
    for i in range(len(lst)):
        pivot = lst[i]
        rest = lst[i+1:]
        count += len([rest[j] for j in range(len(rest)) if pivot > rest[j]])
    return count


print(merge_sort_inversion([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))
