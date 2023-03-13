from copy import deepcopy

def parenthesis_generator(n):
    if n == 0:
        return []
    
    curr = ['(']
    result = _paren(1, n-1, curr)
    for i, v in enumerate(result):
        result[i] = ''.join(v)
    return result


def _paren(already_opened, not_yet_opened, curr_list):
    result = []
    if already_opened == 0 and not_yet_opened == 0:
        result.append(curr_list)
    else:
        if already_opened > 0:
            curr_copy1 = deepcopy(curr_list)
            curr_copy1.append(')')
            result.extend(_paren(already_opened-1, not_yet_opened, curr_copy1))
        if not_yet_opened > 0:
            curr_copy2 = deepcopy(curr_list)
            curr_copy2.append('(')
            result.extend(_paren(already_opened+1, not_yet_opened-1, curr_copy2))
    return result


if __name__ == '__main__':
    for i in range(5):
        print(parenthesis_generator(i))