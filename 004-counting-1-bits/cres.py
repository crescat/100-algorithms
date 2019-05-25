def counting_1_bits(binary_number):
    count = 0
    while binary_number > 0:
        binary_number &= binary_number - 1
        count += 1
    return count


print(counting_1_bits(0b10100101101011101))
