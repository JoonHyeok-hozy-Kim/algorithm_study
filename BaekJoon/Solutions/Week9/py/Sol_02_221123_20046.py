"""
https://www.acmicpc.net/problem/20046
"""
input = __import__('sys').stdin.readline
from math import inf
from collections import deque


def deque_solution(M, N, B, D):
    job_queue = deque()
    job_queue.append([0, 0])
    finished = False
    job_cnt = 0

    while job_queue:
        popped = job_queue.popleft()
        job_cnt += 1
        # print('popped : {}'.format(popped))
        cross_check(M, N, B, D, popped[0], popped[1], job_queue)

    return job_cnt


def cross_check(M, N, B, D, i, j, Q):
    # print('cross_check, i : {}, j : {}'.format(i, j))
    if i > 0 and B[i-1][j] != -1:
        if D[i-1][j] == inf or D[i-1][j] > B[i-1][j] + D[i][j]:
            D[i-1][j] = B[i-1][j] + D[i][j]
            Q.append([i-1, j])

    if i < M-1 and B[i+1][j] != -1:
        if D[i+1][j] == inf or D[i+1][j] > B[i+1][j] + D[i][j]:
            D[i+1][j] = B[i+1][j] + D[i][j]
            Q.append([i+1, j])

    if j > 0 and B[i][j-1] != -1:
        if D[i][j-1] == inf or D[i][j-1] > B[i][j-1] + D[i][j]:
            D[i][j-1] = B[i][j-1] + D[i][j]
            Q.append([i, j-1])

    if j < N-1 and B[i][j+1] != -1:
        if D[i][j+1] == inf or D[i][j+1] > B[i][j+1] + D[i][j]:
            D[i][j+1] = B[i][j+1] + D[i][j]
            Q.append([i, j+1])

    # show_D(D)


def show_D(D):
    width = len(D[0])
    for i in D:
        for j in i:
            if j == inf:
                print('_', end=" ")
            else:
                print(j, end=" ")
        print()
    print()


# import sys
# sys.setrecursionlimit(10**6)
def recursive_solution(M, N, B, D, i=0, j=0):
    if i > 0 and B[i-1][j] != -1:
        if D[i-1][j] == inf or D[i-1][j] > B[i-1][j] + D[i][j]:
            D[i-1][j] = B[i-1][j] + D[i][j]
            recursive_solution(M, N, B, D, i-1, j)

    if i < M-1 and B[i+1][j] != -1:
        if D[i+1][j] == inf or D[i+1][j] > B[i+1][j] + D[i][j]:
            D[i+1][j] = B[i+1][j] + D[i][j]
            recursive_solution(M, N, B, D, i+1, j)

    if j > 0 and B[i][j-1] != -1:
        if D[i][j-1] == inf or D[i][j-1] > B[i][j-1] + D[i][j]:
            D[i][j-1] = B[i][j-1] + D[i][j]
            recursive_solution(M, N, B, D, i, j-1)

    if j < N-1 and B[i][j+1] != -1:
        if D[i][j+1] == inf or D[i][j+1] > B[i][j+1] + D[i][j]:
            D[i][j+1] = B[i][j+1] + D[i][j]
            recursive_solution(M, N, B, D, i, j+1)


from heapq import heappush, heappop
def heap_solution(M, N, B, D):
    heap = []
    heappush(heap, (D[0][0], (0, 0)))
    job_cnt = 0

    while heap:
        popped = heappop(heap)
        job_cnt += 1
        cross_check_for_heap(M, N, B, D, popped[1][0], popped[1][1], heap)

    return job_cnt


def cross_check_for_heap(M, N, B, D, i, j, H):
    # print('cross_check, i : {}, j : {}'.format(i, j))
    if i > 0 and B[i-1][j] != -1:
        if D[i-1][j] == inf or D[i-1][j] > B[i-1][j] + D[i][j]:
            D[i-1][j] = B[i-1][j] + D[i][j]
            heappush(H, (D[i-1][j], (i-1, j)))

    if i < M-1 and B[i+1][j] != -1:
        if D[i+1][j] == inf or D[i+1][j] > B[i+1][j] + D[i][j]:
            D[i+1][j] = B[i+1][j] + D[i][j]
            heappush(H, (D[i+1][j], (i+1, j)))

    if j > 0 and B[i][j-1] != -1:
        if D[i][j-1] == inf or D[i][j-1] > B[i][j-1] + D[i][j]:
            D[i][j-1] = B[i][j-1] + D[i][j]
            heappush(H, (D[i][j-1], (i, j-1)))

    if j < N-1 and B[i][j+1] != -1:
        if D[i][j+1] == inf or D[i][j+1] > B[i][j+1] + D[i][j]:
            D[i][j+1] = B[i][j+1] + D[i][j]
            heappush(H, (D[i][j+1], (i, j+1)))

    # show_D(D)


if __name__ == '__main__':
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(M)]
    if board[0][0] == -1:
        print(-1)

    else:
        dp = [[inf] * N for _ in range(M)]
        dp[0][0] = board[0][0]
        # print(board)
        # print(dp)

        # recursive_solution(M, N, board, dp)

        # deque_cnt = deque_solution(M, N, board, dp)
        # print('deque cnt : {}'.format(deque_cnt))

        # dp = [[inf] * N for _ in range(M)]
        # dp[0][0] = board[0][0]
        heap_cnt = heap_solution(M, N, board, dp)
        # print('heap cnt : {}'.format(heap_cnt))

        if dp[M - 1][N - 1] == inf:
            print(-1)
        else:
            print(dp[M - 1][N - 1])

"""
8 8
0 1 1 1 1 1 1 1 1
0 -1 -1 0 -1 -1 -1 1
0 -1 0 0 0 -1 -1 1
0 -1 0 -1 0 -1 -1 1
0 -1 0 -1 0 -1 -1 1
0 -1 0 -1 0 -1 -1 1
0 -1 0 -1 0 0 0 1
0 0 0 -1 -1 -1 -1 1
"""
