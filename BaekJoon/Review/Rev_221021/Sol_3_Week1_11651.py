"""
https://www.acmicpc.net/problem/11651
"""


def _prior_to(p1, p2):
    if p1[1] < p2[1]:
        return True
    elif p1[1] == p2[1] and p1[0] < p2[0]:
        return True
    return False


def merge_sort(S):
    if len(S) == 1:
        return S

    mid = len(S)//2
    S1 = S[:mid]
    S2 = S[mid:]

    merge_sort(S1)
    merge_sort(S2)
    _merge(S, S1, S2)
    return S


def _merge(S, S1, S2):
    i1 = i2 = 0
    while i1 + i2 < len(S1) + len(S2):
        if i2 == len(S2) or (i1 < len(S1) and _prior_to(S1[i1], S2[i2])):
            S[i1 + i2] = S1[i1]
            i1 += 1
        else:
            S[i1 + i2] = S2[i2]
            i2 += 1
    return S


if __name__ == '__main__':
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    # print(_prior_to(points[0], points[1]))

    for i in merge_sort(points):
        print(*i, sep=" ")

