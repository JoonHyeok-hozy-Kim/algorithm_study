"""
7568. 덩치
https://www.acmicpc.net/problem/7568
"""

def compare(D1, D2):
    # print('In compare, D1 vs D2 : {} vs {}'.format(D1, D2))
    if D1[0] > D2[0] and D1[1] > D2[1]:
        return 1
    elif D1[0] < D2[0] and D1[1] < D2[1]:
        return -1
    return 0


def set_compare(M1, M2):
    # print('In set_compare, M1 vs M2 : {} vs {}'.format(M1, M2))
    result = None
    for d1 in M1:
        for d2 in M2:
            temp_result = compare(d1, d2)
            if result is None:
                result = temp_result
            else:
                if result != temp_result:
                    return 0
    return result


def merge_sort(S):
    # print('In merge_sort, S : {}'.format(S))
    n = len(S)
    if n == 1:
        return [S]

    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]

    R1 = merge_sort(S1)
    R2 = merge_sort(S2)

    # print('In merge_sort, R1 vs R2 : {} vs {}'.format(R1, R2))

    R = _merge(R1, R2)
    return R


def _merge(S1, S2):
    # print('In _merge, S1 vs S2 : {} vs {}'.format(S1, S2))
    one_n = len(S1)
    two_n = len(S2)
    one_cnt = 0
    two_cnt = 0
    result = []
    while one_cnt + two_cnt < one_n + two_n:
        if one_cnt == one_n:
            result.extend(S2[two_cnt:two_n])
            break
        elif two_cnt == two_n:
            result.extend(S1[one_cnt:one_n])
            break
        else:
            m1 = S1[one_cnt]
            m2 = S2[two_cnt]
            comparison = set_compare(m1, m2)
            if comparison == 1:
                result.append(m1)
                one_cnt += 1
            elif comparison == -1:
                result.append(m2)
                two_cnt += 1
            else:
                m1.extend(m2)
                result.append(m1)
                one_cnt += 1
                two_cnt += 1
    return result


if __name__ == '__main__':
    N = int(input())
    d_list = []
    sort_list = []
    for i in range(N):
        d_list.append(list(map(int, input().split())))

    sort_list.append([[d_list[0], d_list[0]], [0]])

    for i in range(1, N):
        cnt = 0
        for j in range(len(sort_list)):
            print('sort_list[j][0][0] : {}'.format(sort_list[j][0][0]))
            print('d_list[i] : {}'.format(d_list[i]))
            comparison1 = compare(sort_list[j][0][0], d_list[i])
            comparison2 = compare(sort_list[j][0][1], d_list[i])
            if comparison1 == -1 and comparison2 == -1:
                print('PT1')
                sort_list.insert(j, [[d_list[i], d_list[i]], [i]])
                break
            elif comparison1 == 1 and comparison2 == 1:
                print('PT2')
                cnt += 1
            else:
                print('PT3')
                new_bound = [
                    [min(sort_list[j][0][0][0], d_list[i][0]), min(sort_list[j][0][0][1], d_list[i][1])],
                    [max(sort_list[j][0][1][0], d_list[i][0]), max(sort_list[j][0][1][1], d_list[i][1])]
                ]
                sort_list[j][0] = new_bound
                sort_list[j][1].append(i)
                break

        if cnt == len(sort_list):
            sort_list.append([[d_list[i], d_list[i]], [i]])

    print(sort_list)
    final = [None] * N

    rank = 1
    for i in range(len(sort_list)):
        for j in sort_list[i][1]:
            final[j] = rank
        rank += len(sort_list[i][1])

    print(*final, sep=" ")


