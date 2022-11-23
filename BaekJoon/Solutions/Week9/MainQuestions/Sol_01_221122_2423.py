"""
https://www.acmicpc.net/problem/2423
"""
from math import inf
from collections import deque


def cross_check(N, M, D, L, i, j):
    # print('cross_check, i : {}, j : {}'.format(i, j))
    Q = deque()
    if i > 0:
        if j > 0:
            # print('Direction up-left : {}'.format(L[i-1][j-1]))
            val = 1 if L[i-1][j-1] == '/' else 0
            if D[i-1][j-1] == inf:
                D[i-1][j-1] = D[i][j] + val
                Q.append((i-1, j-1))
            elif D[i-1][j-1] > D[i][j] + val:
                D[i-1][j-1] = D[i][j] + val
                Q.append((i-1, j-1))

        if j < M:
            # print('Direction up-right : {}'.format(L[i-1][j]))
            val = 0 if L[i-1][j] == '/' else 1
            if D[i-1][j+1] == inf:
                D[i-1][j+1] = D[i][j] + val
                Q.append((i-1, j+1))
            elif D[i-1][j+1] > D[i][j] + val:
                D[i-1][j+1] = D[i][j] + val
                Q.append((i-1, j+1))

    if i < N:
        if j > 0:
            # print('Direction down-left : {}'.format(L[i][j-1]))
            val = 0 if L[i][j-1] == '/' else 1
            if D[i+1][j-1] == inf:
                D[i+1][j-1] = D[i][j] + val
                Q.append((i+1, j-1))
            elif D[i+1][j-1] > D[i][j] + val:
                D[i+1][j-1] = D[i][j] + val
                Q.append((i+1, j-1))

        if j < M:
            # print('Direction down-right : {}'.format(L[i][j]))
            val = 1 if L[i][j] == '/' else 0
            if D[i+1][j+1] == inf:
                D[i+1][j+1] = D[i][j] + val
                Q.append((i+1, j+1))
            elif D[i+1][j+1] > D[i][j] + val:
                D[i+1][j+1] = D[i][j] + val
                Q.append((i+1, j+1))

    # print(' -> D : {}'.format(D))
    # print(' -> Q : {}'.format(Q))
    return Q


if __name__ == '__main__':
    N, M = map(int, input().split())
    linkage = [input() for _ in range(N)]
    if (N+M)%2 != 0:
        print('NO SOLUTION')
    else:
        dp = [[inf]*(M+1) for _ in range(N+1)]
        dp[0][0] = 0
        # print(dp)

        job_queue = deque()
        job_queue.append((0, 0))
        while job_queue:
            popped = job_queue.popleft()
            after_checked = cross_check(N, M, dp, linkage, popped[0], popped[1])
            if after_checked:
                job_queue.extend(after_checked)

        print(dp[N][M])