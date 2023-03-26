from random import randint

def quick_sort(L: list, left=None, right=None) -> None:
    if left is None:
        left, right = 0, len(L)-1
    
    print('quick_sort : {}'.format(L[left:right+1]))
    idx = _partition(L, left, right)
    if left < idx-1:
        quick_sort(L, left, idx-1)
    if idx < right:
        quick_sort(L, idx, right)

def _partition(L, left, right):
    pivot = L[(left + right) // 2]
    print('pivot : {}, _partition : {}'.format(pivot, L[left:right+1]))
    while left <= right:
        while L[left] < pivot:
            left += 1
        while pivot < L[right]:
            right -= 1
        
        if left <= right:
            L[left], L[right] = L[right], L[left]
            left += 1
            right -= 1
    return left


if __name__ == '__main__':
    a = [randint(1, 100) for i in range(10)]
    print(a)
    quick_sort(a)
    print(a)