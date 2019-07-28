# Day 42: Hamming Code
from copy import copy
import random
import math

def encode(parity_bits_length, data):
    n = parity_bits_length + len(data)
    if n != 2 ** parity_bits_length - 1:
        raise Exception('Data length incompatible with parity bits length!')

    hamming_code = [0] * n
    for i in range(parity_bits_length):
        hamming_code[2 ** i - 1] = None

    data_copy = copy(data)
    for i in range(n):
        if hamming_code[i] is not None:
            hamming_code[i] = data_copy.pop(0)

    for i in range(parity_bits_length):
        n = 2 ** i
        l = hamming_code[n-1:]
        ones = 0
        valid_nums = [l[i:i + n] for i in range(0, len(l), n)][::2]
        for sublist in valid_nums:
            ones += count_ones(sublist)
        hamming_code[2 ** i - 1] = ones % 2

    return hamming_code


def count_ones(lst):
    return sum([1 for item in lst if item == 1])


def decode(hamming_code):
    n = len(hamming_code)
    error_pos = -1
    parity_bits_length = int(math.log(n + 1, 2))
    if n != 2 ** parity_bits_length - 1:
        raise Exception('Hamming code length error')

    code_copy = copy(hamming_code)
    parity_bits = []
    for i in range(parity_bits_length):
        parity_bits.append(code_copy[2 ** i - 1])
        code_copy[2 ** i - 1] = None

    # check error
    for i in range(parity_bits_length):
        n = 2 ** i
        l = code_copy[n-1:]
        ones = 0
        valid_nums = [l[i:i + n] for i in range(0, len(l), n)][::2]
        for sublist in valid_nums:
            ones += count_ones(sublist)

        if parity_bits[i] != ones % 2:
            error_pos += n

    if error_pos >= 0:
        if code_copy[error_pos] is not None:
            code_copy[error_pos] ^= 1

    return error_pos, [i for i in code_copy if i is not None]


parity_bits = random.randint(3, 5)
data = [random.randint(0, 1) for _ in range(2 ** parity_bits - 1 - parity_bits)]
code = encode(parity_bits, data)
print('hamming code', data, '->', code)

code[random.randint(0, len(code)-1)] ^= 1
print('with error', code)

error, recon = decode(code)
print('error @', error, '->', recon)

print("Is the data & reconstructed data the same?", data == recon)
