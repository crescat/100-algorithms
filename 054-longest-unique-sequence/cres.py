# Day 54: Longest Unique Sequence

def longest_unique_sequence(s):
    i, j = 0, 0
    x, y = 0, 0

    while j < len(s):
        if s[j] in s[i:j]:
            i += 1
        else:
            j += 1

        if j - i > y - x:
            x, y = i, j

    return s[x:y]


print(longest_unique_sequence("6505626049153740153408485"))
