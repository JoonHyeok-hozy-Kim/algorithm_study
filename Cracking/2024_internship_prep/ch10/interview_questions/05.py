def sparse_search(L, v):
    left = _get_next_val_idx(L, 0)
    right = _get_prev_val_idx(L, len(L)-1)

    while left <= right:
        mid = _get_next_val_idx(L, (left + right) // 2)
        if L[mid] == v:
            return mid
        elif L[mid] > v:
            right = _get_prev_val_idx(L, mid-1)
        else:
            left = _get_next_val_idx(L, mid+1)
    return -1



def _get_next_val_idx(L, i):
    while L[i] == '':
        i += 1
    if i == len(L):
        return -1
    else:
        return i
    
def _get_prev_val_idx(L, i):
    while L[i] == '':
        i -= 1
    if i < 0:
        return -1
    else:
        return i


if __name__ == '__main__':
    print('abc' < 'd')
    a = [
        '',
        '',
        '',
        'abc',
        '',
        '',
        'c',
        'de',
        '',
        '',
    ]

    print(_get_next_val_idx(a, 0))
    print(_get_prev_val_idx(a, len(a)-1))
    print(sparse_search(a, 'c'))
    print(sparse_search(a, 'abc'))

    b = [
        'at',
        '',
        '',
        '',
        'ball',
        '',
        '',
        'car',
        '',
        '',
        'dad',
        '',
        '',
    ]

    print(sparse_search(b, 'ball'))