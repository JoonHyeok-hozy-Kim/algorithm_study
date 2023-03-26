from copy import deepcopy

def merge_sort(S: list, left=0, right=None) -> None:
    if right is None:
        right = len(S)
    
    if right - left <= 1:
        return
    
    mid = (left + right) // 2
    merge_sort(S, left, mid)
    merge_sort(S, mid, right)
    _merge(S, left, mid, right)
    print(S[left:right])

def _merge(S, left, mid, right):
    copy = deepcopy(S)
    i0, i1, i2 = left, left, mid
    while i1 < mid or i2 < right:
        if i1 == mid:
            break
        elif i2 == right or copy[i1] <= copy[i2]:
            S[i0] = copy[i1]
            i1 += 1
        else:
            S[i0] = copy[i2]
            i2 += 1
        i0 += 1


if __name__ == '__main__':
    a = [3,3,8,9,7,1,5,7,8,1,2,3,4,5,3,2]
    merge_sort(a)
    print(a)