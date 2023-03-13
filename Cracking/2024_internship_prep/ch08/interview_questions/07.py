from copy import deepcopy

def permutation1(str):
    S = [[str[0]]]
    for i in range(1, len(str)):
        temp = []
        while S:
            popped = S.pop()
            for j in range(len(popped)+1):
                new = deepcopy(popped)
                new.insert(j, str[i])
                temp.append(new)
        S = temp
    
    for i, s in enumerate(S):
        S[i] = ''.join(s)
    
    return S



def permutation2(str):
    L = list(str)
    temp = _perm(L)
    for i, t in enumerate(temp):
        temp[i] = ''.join(t)
    return temp

def _perm(l):
    if len(l) == 1:
        return [l]

    result = []
    for i, v in enumerate(l):
        new = deepcopy(l)
        new.pop(i)
        temp = _perm(new)
        for t in temp:
            t.insert(0, v)
            result.append(t)
    
    return result



if __name__ == '__main__':
    str = 'abc'
    print(permutation1(str))


    str2 = 'abc'
    print(permutation2(str2))