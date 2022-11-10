"""
https://www.acmicpc.net/problem/10090
"""


def divide_solution(S):
    if len(S) == 1:
        return 0

    mid = len(S)//2
    S1 = S[:mid]
    S2 = S[mid:]

    inversion_cnt = 0
    inversion_cnt += divide_solution(S1)
    inversion_cnt += divide_solution(S2)
    inversion_cnt += merge_sort_and_count_inversions(S, S1, S2)
    # print('At {}, {}'.format(S, inversion_cnt))

    return inversion_cnt


def merge_sort_and_count_inversions(S, S1, S2):
    i1 = i2 = 0
    inv_cnt = 0

    # print('In merge_sort_and_count_inversions, {} vs {}'.format(S1, S2))
    while i1+i2 < len(S1)+len(S2):
        if i2 == len(S2) or (i1 < len(S1) and S1[i1] <= S2[i2]):
            S[i1+i2] = S1[i1]
            i1 += 1
        else:
            if i1 < len(S1):
                # print('({}-{})'.format(S1[i1],S2[i2]))
                inv_cnt += len(S1)-i1
            S[i1+i2] = S2[i2]
            i2 += 1
        # print(inv_cnt, S)

    return inv_cnt


if __name__ == '__main__':
    N = int(input())
    series = list(map(int, input().split()))
    # print(series)

    print(divide_solution(series))