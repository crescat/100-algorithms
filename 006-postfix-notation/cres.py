# Day 6 Postfix notation
# input form: '4 5 + 9 1 - *' => 72

def calc(s):
    lst = s.split()
    result = []
    operators = ['+', '-', '*', '/']
    for x in lst:
        if x in operators:
            if x == '+':
                result[-2:] += [result[-2] + result[-1]]
            elif x == '-':
                result[-2:] += [result[-2] - result[-1]]
            elif x == '*':
                result[-2:] += [result[-2] * result[-1]]
            elif x == '/':
                result[-2:] += [result[-2] / result[-1]]
        
        else:
            result += [float(x)]
    
    return result[0]

print(calc('4 5 + 9 1 - *'))