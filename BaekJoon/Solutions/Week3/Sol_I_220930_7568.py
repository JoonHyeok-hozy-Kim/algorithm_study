"""
7568. 덩치
https://www.acmicpc.net/problem/7568
"""
from collections import deque

def compare(D1, D2):
    # print('In compare, D1 vs D2 : {} vs {}'.format(D1, D2))
    # if D1[0] >= D2[0] and D1[1] >= D2[1]:
    #     if not (D1[0] == D2[0] and D1[1] == D2[1]):
    #         return 1
    # elif D1[0] <= D2[0] and D1[1] <= D2[1]:
    #     if not (D1[0] == D2[0] and D1[1] == D2[1]):
    #         return -1


    if D1[0] > D2[0] and D1[1] > D2[1]:
        return 1
    elif D1[0] < D2[0] and D1[1] < D2[1]:
        return -1
    return 0


def merge_sort_buckets(B):
    n = len(B)
    if n == 1:
        return

    mid = n // 2
    B1 = B[0:mid]
    B2 = B[mid:n]

    merge_sort_buckets(B1)
    merge_sort_buckets(B2)

    _merge_buckets(B, B1, B2)


def _merge_buckets(B, B1, B2):
    one_n, two_n = len(B1), len(B2)
    one_cnt, two_cnt = 0, 0
    while one_cnt + two_cnt < one_n + two_n:
        if one_cnt == one_n:
            while two_cnt < two_n:
                B[one_cnt+two_cnt] = B2[two_cnt]
                two_cnt += 1
        elif two_cnt == two_n:
            while one_cnt < one_n:
                B[one_cnt+two_cnt] = B1[one_cnt]
                one_cnt += 1
        else:
            if B1[one_cnt][0][0] > B2[two_cnt][0][0]:
                B[one_cnt+two_cnt] = B1[one_cnt]
                one_cnt += 1
            else:
                B[one_cnt+two_cnt] = B2[two_cnt]
                two_cnt += 1


if __name__ == '__main__':
    N = int(input())
    d_list = []
    for i in range(N):
        d_list.append(list(map(int, input().split())))

    # print(d_list)
    for i in range(len(d_list)):
        rank_cnt = 0
        for j in range(len(d_list)):
            if i != j:
                if compare(d_list[i], d_list[j]) == -1:
                    rank_cnt += 1
        print(rank_cnt+1, end=" ")

