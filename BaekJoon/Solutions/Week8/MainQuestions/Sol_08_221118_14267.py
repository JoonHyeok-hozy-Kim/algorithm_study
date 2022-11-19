"""
https://www.acmicpc.net/problem/14267
"""
import sys
sys.setrecursionlimit(10**5)


def dfs_with_weigth_accumulation(T, D, P, i=1, a_w=0):
    new_weight = P[i] if i in P else 0
    D[i] = a_w + new_weight
    # print('In dfs_with_weigth_accumulation, D : {}'.format(D))
    for child in T[i]:
        dfs_with_weigth_accumulation(T, D, P, child, a_w+new_weight)


if __name__ == '__main__':
    N, M = map(int, input().split())
    tree_list = [[] for _ in range(N+1)]
    dp = [0] * (N+1)
    employee_num = 1
    for boss in map(int, input().split()):
        # print('boss : {}, employee_num : {}'.format(boss, employee_num))
        if employee_num > 1:
            tree_list[boss].append(employee_num)
        employee_num += 1
    # print('tree_list : {}'.format(tree_list))

    praise_record = {}
    for _ in range(M):
        praised, weight = map(int, input().split())
        if praised not in praise_record:
            praise_record[praised] = weight
        else:
            praise_record[praised] += weight

    dfs_with_weigth_accumulation(tree_list, dp, praise_record)
    # dp.pop(0)
    # print(*dp, sep=" ")
    for i in range(N):
        print(dp[i+1], end=" ")
