# Day 47: Factoradic

from math import factorial

def dec_to_fac(num):
    quotient = num
    remainders = []
    while True:
        quotient, remainder = divmod(quotient, len(remainders)+1)
        remainders.append(remainder)
        if quotient == 0:
            return int(''.join([str(i) for i in remainders[::-1]]))


def fac_to_dec(num):
    fac = str(num)[::-1]
    return sum([factorial(i) * int(n) for i, n in enumerate(fac)])


print(dec_to_fac(463))
print(fac_to_dec(341010))
print(fac_to_dec(dec_to_fac(800)))
