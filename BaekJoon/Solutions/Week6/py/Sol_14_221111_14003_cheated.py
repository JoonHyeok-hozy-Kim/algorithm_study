"""
https://www.acmicpc.net/problem/14003
"""


def binary_search(A, v):
    start, end = 0, len(A)
    while start <= end:
        mid = (start + end) // 2
        if A[mid] >= v:
            end = mid-1
        else:
            start = mid+1
    return start


if __name__ == '__main__':
    N = int(input())
    series = list(map(int, input().split()))
    # print(series)

    dp = [None] * N
    dp[0] = 0
    L = [series[0]]
    for i in range(1, N):
        if series[i] > L[-1]:
            dp[i] = len(L)
            L.append(series[i])

        else:
            idx = binary_search(L, series[i])
            dp[i] = idx
            L[idx] = series[i]

        # print(dp, L)

    lis = []
    j = N-1
    k = len(L)-1
    while j >= 0 and k >= 0:
        if dp[j] == k:
            lis.append(series[j])
            k -= 1
        else:
            j -= 1

    print(len(L))
    print(*reversed(lis), sep=" ")

"""
7
10 50 60 40 20 70 5
"""