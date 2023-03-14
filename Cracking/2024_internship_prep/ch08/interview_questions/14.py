from itertools import permutations
from copy import deepcopy

def parse_expression(exp):
    symbols = []
    operators = []
    for c in exp:
        if c in ('&', '|', '^'):
            operators.append(c)
        else:
            symbols.append(int(c))
    return symbols, operators

def operate(symbols, operators, oi):
    if operators[oi] == '&':
        temp = symbols[oi] & symbols[oi+1]
    elif operators[oi] == '|':
        temp = symbols[oi] | symbols[oi+1]
    elif operators[oi] == '^':
        temp = symbols[oi] ^ symbols[oi+1]
    symbols.pop(oi)
    symbols[oi] = temp
    operators.pop(oi)

def show_expression(s, o):
    idx = 0
    while idx < len(o):
        print(s[idx], end="")
        print(o[idx], end="")
        idx += 1
    print(s[idx])

def boolean_evaluation(exp, desired_result):
    symbols, operators = parse_expression(exp)
    # show_expression(symbols, operators)
    return _inner(symbols, operators, desired_result)

def _inner(symbols, operators, desired_result, depth=0):
    if len(symbols) == 1 and symbols[0] == desired_result:
        return 1
    
    for i in range(depth):
        print(" ", end="")
    show_expression(symbols, operators)
    result = 0
    for i in range(len(operators)):
        cs, co = deepcopy(symbols), deepcopy(operators)
        operate(cs, co, i)
        result += _inner(cs, co, desired_result, depth+1)
    return result


if __name__ == '__main__':
    # print(boolean_evaluation("1^0|0|1", 0))
    print(boolean_evaluation("0&0&0&1^1|0", 1))
