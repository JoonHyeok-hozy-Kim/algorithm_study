def search_in_rotated_array(A, k, left=None, right=None):
    if left is None:
        left, right = 0, len(A)-1
    print('search_in_rotated_array, {}'.format(A[left:right+1]))
    mid = (left + right) // 2
    if k == A[mid]:
        return mid
    
    if A[left] < A[mid]:
        if A[left] <= k < A[mid]:
            return _binary_search(A, k, left, mid-1)
        else:
            return search_in_rotated_array(A, k, mid+1, right)
    else:
        if A[mid] < k <= A[right]:
            return _binary_search(A, k, mid+1, right)
        else:
            return search_in_rotated_array(A, k, left, mid-1)

    
def _binary_search(A, k, left, right):
    print('_binary_search, {}'.format(A[left:right+1]))
    while left <= right:
        mid = (left + right) // 2
        if k == A[mid]:
            return mid
        elif k < A[mid]:
            right = mid-1
        else:
            left = mid+1
    return left


if __name__ == '__main__':
    a = [i for i in range(10)]
    for i in range(3):
        a.insert(0, a.pop())
    print(a)
    print(search_in_rotated_array(a, 3))
    print(search_in_rotated_array(a, 9))