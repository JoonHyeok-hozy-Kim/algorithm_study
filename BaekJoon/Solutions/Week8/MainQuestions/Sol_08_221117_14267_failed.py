"""
https://www.acmicpc.net/problem/14267
"""
# import sys
# sys.setrecursionlimit(10**5)
#
#
# def traverse(T, D, i, w):
#     # print('In traverse, i : {}, w : {}'.format(i, w))
#     D[i] += w
#     for follower in T[i]:
#         traverse(T, D, follower, w)
#     # print(D)


from collections import deque


def loop_traverse(T, D, i, w):
    Q = deque()
    Q.append(i)
    while Q:
        popped = Q.popleft()
        D[popped] += w
        for follower in T[popped]:
            Q.append(follower)


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

    for _ in range(M):
        praised, weight = map(int, input().split())
        # traverse(tree_list, dp, praised, weight)
        loop_traverse(tree_list, dp, praised, weight)

    # dp.pop(0)
    # print(*dp, sep=" ")
    for i in range(N):
        print(dp[i+1], end=" ")