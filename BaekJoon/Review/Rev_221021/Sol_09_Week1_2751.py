"""
https://www.acmicpc.net/problem/2751
"""


def merge_sort(S):
    if len(S) == 1:
        return S

    n = len(S)
    mid = n//2
    S1 = S[:mid]
    S2 = S[mid:]

    merge_sort(S1)
    merge_sort(S2)
    _merge(S, S1, S2)
    return S


def _merge(S, S1, S2):
    i1 = i2 = 0
    while i1 + i2 < len(S1) + len(S2):
        if i2 == len(S2) or (i1 < len(S1) and S1[i1] <= S2[i2]):
            S[i1 + i2] = S1[i1]
            i1 += 1
        else:
            S[i1 + i2] = S2[i2]
            i2 += 1
    return S


if __name__ == '__main__':
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    # print(nums)

    # for i in sorted(nums):
    #     print(i)

    for i in merge_sort(nums):
        print(i)