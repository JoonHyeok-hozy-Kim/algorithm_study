def binary_search(L: list, target: int) -> int:
    left, right = 0, len(L)
    
    while left < right:
        mid = (left + right) // 2
        if L[mid] == target:
            return mid
        elif L[mid] > target:
            right = mid
        else:
            left = mid+1
    
    return -1


if __name__ == '__main__':
    a = [i for i in range(10)]
    print(a)
    print(binary_search(a, 5))
    print(binary_search(a, 10))
    print(binary_search(a, -1))