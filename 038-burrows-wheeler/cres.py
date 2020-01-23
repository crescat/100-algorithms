# Day 38: Burrows-Wheeler

def encode(s):
    l = [x for x in s]
    mtx = []
    for i in range(len(s)):
        mtx += [l[-i:]+l[:-i]]
    sorted_mtx = sorted(mtx)
    idx = sorted_mtx.index(l)
    result = ''.join([x[-1] for x in sorted_mtx])
    return result, idx


def decode(s, idx):
    length = len(s)
    mtx = [''] * length
    for i in range(length):
        mtx = sorted([a + b for a, b in zip(s, mtx)])
    return mtx[idx]


s = 'Mary had a little lamb'
result, idx = encode(s)
print('encoded string is "{}", index is {}'.format(result, idx))
decoded = decode(result, idx)
print('decoded string is "{}"'.format(decoded))
