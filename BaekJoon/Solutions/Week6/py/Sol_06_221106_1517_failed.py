"""
https://www.acmicpc.net/problem/1517
"""


def binary_search1(A, v):
    start, end = 0, len(A)-1
    while end > start:
        mid = (start + end) // 2
        # print('s : {}, m : {}, e : {} / A[m] : {}'.format(start, mid, end, A[mid]))
        if A[mid] >= v:
            end = mid
        else:
            start = mid+1

    return start


def binary_search2(A, v):
    start, end = 0, len(A)-1
    while end > start:
        mid = (start + end) // 2 + 1
        # print('s : {}, m : {}, e : {} / A[m] : {}'.format(start, mid, end, A[mid]))
        if A[mid] > v:
            end = mid - 1
        else:
            start = mid

    return start



if __name__ == '__main__':
    # a = [2, 4, 6, 8]
    # print(binary_search1(a, 3))
    # print(binary_search1(a, 4))
    # print(binary_search1(a, 5))
    # print(binary_search1(a, 6))
    # print(binary_search1(a, 8))

    # a = [2, 4, 4, 4, 6]
    # print(binary_search2(a, 4))


    N = int(input())
    L = []
    result = 0
    for i in map(int, input().split()):
        if len(L) == 0 or i >= L[-1]:
            L.append(i)

        else:
            target_idx = binary_search2(L, i)
            # print('target_idx : {}'.format(target_idx))
            if L[target_idx] == i:
                result += len(L) - target_idx - 1
            else:
                result += len(L) - target_idx
            L.insert(target_idx, i)

        # print(result, L)

    print(result)


"""
5
1 2 1 3 2
"""