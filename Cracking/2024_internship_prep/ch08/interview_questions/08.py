from copy import deepcopy

def permutations_with_duplicates(str):
    M = {}
    for c in str:
        if c in M:
            M[c] += 1
        else:
            M[c] = 1
    chars = [k for k in M.keys()]
    cnts = [M[c] for c in chars]
    result = _perm(chars, cnts)
    for i, r in enumerate(result):
        result[i] = ''.join(r)
    return result

def _perm(chars, cnts):
    result = []
    if len(chars) == 1:
        result.append([chars[0] for k in range(cnts[0])])
    else:
        for i, c in enumerate(chars):
            copy_chars, copy_cnts = deepcopy(chars), deepcopy(cnts)
            if copy_cnts[i] > 1:
                copy_cnts[i] -= 1
                temp = _perm(copy_chars, copy_cnts)
            else:
                copy_chars.pop(i)
                copy_cnts.pop(i)
                temp = _perm(copy_chars, copy_cnts)
            for t in temp:
                t.insert(0, c)
                result.append(t)
    return result



if __name__ == '__main__':
    a = 'a'
    print(permutations_with_duplicates(a))
    a = 'aaaa'
    print(permutations_with_duplicates(a))
    
    a = 'ab'
    print(permutations_with_duplicates(a))
    a = 'abc'
    print(permutations_with_duplicates(a))
    a = 'aabc'
    print(permutations_with_duplicates(a))