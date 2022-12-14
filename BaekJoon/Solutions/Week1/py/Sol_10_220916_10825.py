"""
10825. 국영수
https://www.acmicpc.net/problem/10825
"""

def comes_first(s1, s2):
    # print('Compare {} vs {}'.format(s1, s2))
    # Decreasing order : 국어
    if s1[1] > s2[1]:
        return True
    elif s1[1] == s2[1]:
        # Increasing order : 영어
        if s1[2] < s2[2]:
            return True
        elif s1[2] == s2[2]:
            # Decreasing order : 수학
            if s1[3] > s2[3]:
                return True
            elif s1[3] == s2[3]:
                # Lexicographically Increasing order : Name
                if s1[0] < s2[0]:
                    return True
    return False


def _merge_array(S, S1, S2):
    one_idx = 0
    two_idx = 0
    while one_idx + two_idx < len(S):
        if two_idx == len(S2) or (one_idx < len(S1) and comes_first(S1[one_idx], S2[two_idx])):
            S[one_idx + two_idx] = S1[one_idx]
            one_idx += 1
        else:
            S[one_idx + two_idx] = S2[two_idx]
            two_idx += 1
    return


def merge_sort(S):
    n = len(S)

    if n <= 1:
        return

    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]

    merge_sort(S1)
    merge_sort(S2)
    _merge_array(S, S1, S2)
    return

if __name__ == '__main__':
    student_num = int(input())
    database = []
    for i in range(student_num):
        row = []
        data = input().split()
        row.append(data[0])
        for i in range(3):
            row.append(int(data[i+1]))
        database.append(row)
    # print(database)
    merge_sort(database)
    # print(database)
    for student in database:
        print(student[0])