# Day 7: Binary addition FSA

q0 = {
    ('0', '0'): ('q0', '0'),
    ('1', '0'): ('q0', '1'),
    ('0', '1'): ('q0', '1'),
    ('1', '1'): ('q1', '0')
}

q1 = {
    ('0', '0'): ('q0', '1'),
    ('1', '0'): ('q1', '0'),
    ('0', '1'): ('q1', '0'),
    ('1', '1'): ('q1', '1')
}

def add_binary(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    length = max(len(s1), len(s2)) + 1
    n1 = s1.rjust(length, '0')[::-1]
    n2 = s2.rjust(length, '0')[::-1]
    state = 'q0'
    result = ''

    for x in zip(n1, n2):
        if state == 'q0':
            state, y = q0[x]
            result += y

        elif state == 'q1':
            state, y = q1[x]
            result += y

    return result[::-1].lstrip('0')


print(add_binary(1100100100100, 100100011000))
