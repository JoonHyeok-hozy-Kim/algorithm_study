"""
https://www.acmicpc.net/problem/1654
"""
from bisect import bisect_right


def binary_search(A, v):
    start, end = 0, len(A)
    while end > start:
        mid = (start + end) // 2
        if A[mid] == v:
            return mid
        elif A[mid] > v:
            end = mid - 1
        else:
            start = mid + 1
    return start


def max_line_cut(K, N, L):
    for i in range(1, N+1):
        target_cut = L[-1] // i
        remaining = len(L) - bisect_right(L, target_cut)
        print(target_cut, remaining)




if __name__ == '__main__':
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]
    # print(lines)

    lines.sort()
    max_line_cut(K, N, lines)