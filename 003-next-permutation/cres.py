# Day 3: Next permutation

def next_p(s):
    for i in range(-1, -len(s), -1):
        if s[i-1] < s[i]:
            pivot = s[i-1]
            left = s[:i-1]
            right = s[i:]
            break
    
    higher_min = min([x for x in right if x > pivot])
    min_index = right.index(higher_min)
    new_right = right[:min_index] + pivot + right[min_index+1:]
    return left + higher_min + ''.join(sorted(new_right))

print(next_p('FAED'))
    