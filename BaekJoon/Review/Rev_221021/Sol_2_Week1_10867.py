"""
https://www.acmicpc.net/problem/10867
"""


def no_repeat_merge_sort(S):
    if len(S) == 1:
        return S

    mid = len(S)//2
    S1 = S[:mid]
    S2 = S[mid:]

    S1 = no_repeat_merge_sort(S1)
    S2 = no_repeat_merge_sort(S2)

    return _merge(S1, S2)


def _merge(S1, S2):
    new_s = [None] * (len(S1)+len(S2))
    # print('In _merge, {} vs {}'.format(S1, S2))
    i1 = i2 = 0
    rep_cnt = 0
    while i1 + i2 < len(S1) + len(S2):
        if i1 < len(S1) and i2 < len(S2):
            if S1[i1] < S2[i2]:
                new_s[i1 + i2 - rep_cnt] = S1[i1]
                i1 += 1
            elif S1[i1] > S2[i2]:
                new_s[i1 + i2 - rep_cnt] = S2[i2]
                i2 += 1
            else:
                new_s[i1 + i2 - rep_cnt] = S1[i1]
                rep_cnt += 1
                i1 += 1
                i2 += 1
        elif i1 == len(S1):
            new_s[i1 + i2 - rep_cnt] = S2[i2]
            i2 += 1
        else:
            new_s[i1 + i2 - rep_cnt] = S1[i1]
            i1 += 1

    # print(' before pop, rep_cnt : {}, new_s : {}'.format(rep_cnt, new_s))
    for j in range(rep_cnt):
        new_s.pop()
        # S[(j+1)*(-1)] = None
    # print(' ㄴ result : {}'.format(new_s))
    return new_s


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    final = no_repeat_merge_sort(nums)
    print(*final, sep=" ")