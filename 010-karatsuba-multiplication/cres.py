def karatsuba_mult(a, b):
    binary_a = bin(a)[::-1]
    result = 0
    for i in range(len(binary_a)):
        if binary_a[i] == '1':
            result += b * 2 ** i
    return result

print(karatsuba_mult(75431456753245638765348576526448776785674432343578843623, \
    243562124645233647544337879708765452634856756467657542324467543214))
