"""
https://www.acmicpc.net/problem/1517
"""


def swap_counting_merge_sort(S):
    if len(S) == 1:
        return S, 0

    mid = len(S)//2
    S1 = S[:mid]
    S2 = S[mid:]
    S1, cnt1 = swap_counting_merge_sort(S1)
    S2, cnt2 = swap_counting_merge_sort(S2)

    return _merge(S1, S2, cnt1 + cnt2)


def _merge(S1, S2, prev_cnt):
    i1 = i2 = 0
    SS = [None] * (len(S1) + len(S2))
    curr_cnt = prev_cnt
    while i1 + i2 < len(S1) + len(S2):
        if i2 == len(S2) or (i1 < len(S1) and S1[i1] <= S2[i2]):
            SS[i1 + i2] = S1[i1]
            i1 += 1
        else:
            SS[i1 + i2] = S2[i2]
            i2 += 1
            curr_cnt += len(S1) - i1
    return SS, curr_cnt


if __name__ == '__main__':
    N = int(input())
    series = list(map(int, input().split()))

    S, cnt = swap_counting_merge_sort(series)
    # print(S)
    print(cnt)

"""
5
1 2 1 3 2
"""