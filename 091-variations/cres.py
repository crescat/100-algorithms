# Day 91: Variations
from itertools import permutations

perms = [0] + [int(''.join(p)) for i in range(1, 11)
                               for p in permutations('0123456789', i)
                               if p[0] != '0']

def variation_to_order(variation):
    return perms.index(variation)

def order_to_variation(order):
    return perms[order]

print(order_to_variation(4444444))
print(variation_to_order(32568741))
