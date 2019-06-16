# Day 15: Breaking OTP

import string
import random

def decode(ciphertext):
    valid_letters = set(string.ascii_lowercase) | {' '}
    result = [''] * len(ciphertext)

    for chars in zip(*ciphertext):
        keys = set()

        for i in range(256):
            if all(chr(c ^ i) in valid_letters for c in chars):
                keys.add(i)

        if len(keys) == 1:
            key = list(keys)[0]
        else:
            key = False

        for i in range(len(result)):
            if key:
                result[i] += chr(chars[i] ^ key)
            else:
                result[i] += '?'

    return result


def generate_keys(length):
    return [random.randint(0, 255) for _ in range(length)]


def encrypt(text, keys):
    result = [ord(text[i])^keys[i] for i in range(len(text))]
    return bytes(result)


def decrypt(ciphertext, keys):
    result = [chr(ciphertext[i]^keys[i]) for i in range(len(ciphertext))]
    return ''.join(result)


def print_by_lines(lst):
    for line in lst:
        print(line)


text = [
"take this kiss upon t",
"and in parting from y",
"thus much let me avow",
"you are not wrong who",
"that my days have bee",
"yet if hope has flown",
"in a night or in a da",
"in a vision or in non",
"is it therefore the l",
"all that we see or se",
"is but a dream within",
"i stand amid the roar",
"of a surf tormented s",
"and i hold within my ",
"grains of the golden ",
"how few yet how they ",
"through my fingers to",
"while i weep while i ",
"o god can i not grasp",
"them with a tighter c",
"o god can i not save ",
"one from the pitiless",
"is all that we see or",
"but a dream within a "
]

keys = generate_keys(len(text[0]))

ciphertext = [encrypt(line, keys) for line in text]
print_by_lines(decode(ciphertext))
