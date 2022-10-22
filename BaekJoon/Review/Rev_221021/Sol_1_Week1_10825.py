"""
https://www.acmicpc.net/problem/10825
"""


def _comes_first(s1, s2):
    # 국어 감소
    if int(s1[1]) > int(s2[1]):
        return True
    elif int(s1[1]) < int(s2[1]):
        return False
    else:
        # 영어 증가
        if int(s1[2]) < int(s2[2]):
            return True
        elif int(s1[2]) > int(s2[2]):
            return False
        else:
            # 수학 감소
            if int(s1[3]) > int(s2[3]):
                return True
            elif int(s1[3]) < int(s2[3]):
                return False
            else:
                # 사전 순 증가
                if s1[0] < s2[0]:
                    return True
                else:
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
        if i2 == len(S2) or (i1 < len(S1) and _comes_first(S1[i1], S2[i2])):
            S[i1 + i2] = S1[i1]
            i1 += 1
        else:
            S[i1 + i2] = S2[i2]
            i2 += 1


if __name__ == '__main__':
    N = int(input())
    students = [input().split() for _ in range(N)]
    # print(students)
    # print(students[0], students[1])
    # print(_comes_first(students[0], students[1]))

    merge_sort(students)
    # print(students)
    for s in students:
        print(s[0])