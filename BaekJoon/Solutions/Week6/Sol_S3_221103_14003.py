"""
https://www.acmicpc.net/problem/14003
"""


def recursive_binary_search(A, v, start=None, end=None):
    if start is None:
        start, end = 0, len(A)

    # print('In binary, v : {}, A : {}, s : {}, e : {}'.format(v, A, start, end))
    if end - start == 1:
        if A[start] >= v:
            return start
        else:
            return start+1
        
    mid = (start + end)//2
    if v == A[mid]:
        return mid
    elif v < A[mid]:
        return recursive_binary_search(A, v, start, mid)
    else:
        return recursive_binary_search(A, v, mid+1, end)


def loop_binary_search(A, v):
    start, end = 0, len(A)
    while end - start > 1:
        mid = (start + end)//2
        if A[mid] == v:
            return mid
        elif A[mid] > v:
            end = mid
        else:
            start = mid+1

    if A[start] >= v:
        return start
    else:
        return start + 1



if __name__ == '__main__':

    # a = [i*2 for i in range(10)]
    # print(a)
    # print(binary_search(a, 6))
    # print(binary_search(a, 7))
    # print(binary_search(a, 8))

    # from math import log2
    # print(log2(1000000))


    N = int(input())
    series = list(map(int, input().split()))
    # print(series)

    dp = [None] * N
    dp[0] = 0
    lis = [series[0]]

    for i in range(1, N):
        if series[i] > lis[-1]:
            dp[i] = len(lis)
            lis.append(series[i])

        else:
            # idx = recursive_binary_search(lis, series[i])
            idx = loop_binary_search(lis, series[i])
            dp[i] = idx
            lis[idx] = series[i]

        # print(dp)
        # print(lis)

    print(len(lis))
    result = []
    k = len(lis)-1
    j = N-1
    while k >= 0 and j >= 0:
        if dp[j] == k:
            result.append(str(series[j]))
            k -= 1
        j -= 1
    # print(' '.join(reversed(result)))
    print(*reversed(result), sep=" ")