# Day 29: String searching

def find_index(s):
    letters = set(s)
    return {letter:s[::-1].index(letter)+1 for letter in letters}


def search(s, pattern):
    index_table = find_index(pattern)
    i, l = 0, len(pattern)
    result = []
    while True:
        if s[i:i+l] == pattern:
            result.append(i)
        if i + l < len(s):
            i += index_table.get(s[i+l], l+1)
        else:
            break

    if result == []:
        return "pattern '{}' not found!".format(pattern)
    elif len(result) == 1:
        return "pattern '{}' found at position {}".format(pattern, result[0])
    else:
        result_str = "pattern '{}' found at position {}" + \
                     ", position {}" * (len(result) - 2) + \
                     " and position {}"
        return result_str.format(pattern, *result)


print(search("The rose is red, the violet's blue, Sugar's sweet and so are you.", 'rose'))
