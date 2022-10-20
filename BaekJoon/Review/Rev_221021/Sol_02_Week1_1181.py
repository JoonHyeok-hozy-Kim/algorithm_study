"""
https://www.acmicpc.net/problem/1181
"""

def _come_first(w1, w2):
    if len(w1) < len(w2):
        return True
    elif len(w1) == len(w2):
        for i in range(len(w1)):
            if w1[i] < w2[i]:
                return True
            elif w1[i] > w2[i]:
                break

    return False


def merge_sort(S):
    # print('In merge_sort, S : {}'.format(S))
    n = len(S)
    if n == 1:
        return S
    mid = n//2
    S1 = S[:mid]
    S2 = S[mid:]

    merge_sort(S1)
    merge_sort(S2)
    _merge(S, S1, S2)

    # print('After merge, S : {}'.format(S))
    return S


def _merge(S, S1, S2):
    # print('In _merge, {} vs {}'.format(S1, S2))
    one_idx, two_idx = 0, 0
    while one_idx + two_idx < len(S1) + len(S2):
        # print(one_idx, two_idx)
        if two_idx == len(S2) or (one_idx < len(S1) and _come_first(S1[one_idx], S2[two_idx])):
            S[one_idx+two_idx] = S1[one_idx]
            one_idx += 1
        else:
            S[one_idx+two_idx] = S2[two_idx]
            two_idx += 1


if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    # print(words)

    merge_sort(words)
    prev = None
    for w in words:
        if prev is None or prev != w:
            print(w)
            prev = w