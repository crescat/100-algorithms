# Day 37: Longest Common Subsequence

def lcr_length(a, b):
    def helper(a, b, i, j):
        if i < 0 or j < 0:
            return 0
        elif a[i] == b[j]:
            return 1 + helper(a, b, i-1, j-1)
        else:
            return max(helper(a, b, i-1, j), helper(a, b, i, j-1))

    return helper(a, b, len(a)-1, len(b)-1)


a = 'abcde'
b = 'ahbec'
print(lcr_length(a, b))
