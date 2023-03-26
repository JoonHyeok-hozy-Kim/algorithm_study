def anagram_sort(L):
    M = [_modifier(s) for s in L]
    # print('M : {}'.format(M))
    merge_sort(M)
    for i, m in enumerate(M):
        L[i] = m[2]

def _modifier(S):
    result = [len(S), [0] * 26, S]
    for c in S:
        result[1][ord(c)-ord('a')] += 1
    return result

def _smaller(m1, m2):
    if m1[0] < m2[0]:
        return True
    elif m1[0] > m2[0]:
        return False
    else:
        for i in range(26):
            if m1[1][i] < m2[1][i]:
                return True
            elif m1[1][i] > m2[1][i]:
                return False
    return True

def merge_sort(L):
    if len(L) <= 1:
        return L
    
    mid = len(L)//2
    l1 = merge_sort(L[0:mid])
    l2 = merge_sort(L[mid:])
    _merge(L, l1, l2)
    return L

def _merge(L, l1, l2):
    i1 = i2 = 0
    while i1 + i2 < len(L):
        if i2 == len(l2) or (i1 < len(l1) and _smaller(l1[i1], l2[i2])):
            L[i1+i2] = l1[i1]
            i1 += 1
        else:
            L[i1+i2] = l2[i2]
            i2 += 1

if __name__ == '__main__':
    l = [
        'abc',
        'a',
        'za',
        'cba',
        'bbb',
        'az',
        'kspp',
        'ppsk',
        'zzz',
        'bac',
        'bbc',
        'ccc',
    ]
    
    print(l)
    anagram_sort(l)
    print(l)