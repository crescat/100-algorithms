# Day 39: 4-sum

def find_4_sum(lst, n):
    # store pair sums
    pair_sums = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            pairsum = lst[i] + lst[j]
            pair_sums.append((pairsum, (i, j)))

    result = set()
    for i in range(len(pair_sums)-1):
        for j in range(i+1, len(pair_sums)):
            foursum = pair_sums[i][0] + pair_sums[j][0]
            if foursum == n:
                idx = pair_sums[i][1] + pair_sums[j][1]
                if len(set(idx)) == 4:
                    result.add(tuple(sorted(lst[i] for i in idx)))

    if len(result) == 0:
        return 'No quadruplets with sum {} found'.format(n)
    else:
        return result


print(find_4_sum([1,2,3,4,5,6,7,8,9], 15))
