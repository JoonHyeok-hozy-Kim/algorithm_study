def magic_index_distinct_array(arr):
    return _distinct_inner(arr, 0, len(arr))

def _distinct_inner(arr, start, end):
    if start == end:
        return None

    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif start < mid < arr[mid]:
        return _distinct_inner(arr, start, mid)
    else:
        return _distinct_inner(arr, mid+1, end)


def magic_index_repeated_array(arr):
    return _repeated_inner(arr, 0, len(arr))

def _repeated_inner(arr, start, end):
    if start == end:
        return None
    
    mid = (start + end) // 2
    if mid == arr[mid]:
        return mid
    if arr[start] <= start:
        temp = _repeated_inner(arr, start, mid)
        if temp is not None:
            return temp
        
    if end-1 <= arr[end-1]:
        temp = _repeated_inner(arr, mid+1, end)
        if temp is not None: 
            return temp
    
    return None


if __name__ == '__main__':
    test1 = [-3, -1, 2, 4, 7, 8, 10, 11]
    print(magic_index_distinct_array(test1))
    test2 = [-3, -1, 0, 1, 2, 5, 8, 10]
    print(magic_index_distinct_array(test2))
    test3 = [-3, -1, 0, 1, 2, 6, 8, 10]
    print(magic_index_distinct_array(test3))
    test4 = [-3, -1, 0, 1, 2, 4, 5, 7]
    print(magic_index_distinct_array(test4))

    print("--------------Repeat Test--------------")
    test5 = [-3, -3, -3, -3, -3, -3, -3, 7]
    print(magic_index_repeated_array(test5))

    test6 = [-10, -5, 2, 2, 2, 3, 4, 11, 13]
    print(magic_index_repeated_array(test6))

    test6 = [-10, -5, 1, 2, 2, 3, 4, 6, 8]
    print(magic_index_repeated_array(test6))


    # 146