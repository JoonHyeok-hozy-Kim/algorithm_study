"""
https://www.acmicpc.net/problem/23258
"""
input = __import__('sys').stdin.readline
from collections import deque


def first_fill(N, D, F):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if D[start][end] > 0:
                F[start][end] = [D[start][end], 0]
    # print('first_fill, F : {}'.format(F))


def generate_floyd_warshall_job_queue(N):
    Q = deque()
    for mid in range(1, N+1):
        for start in range(1, N+1):
            if mid == start:
                continue
            for end in range(1, N+1):
                if start == end or mid == end:
                    continue
                Q.append((start, mid, end))
    return Q


def floyd_warshall(D, F, max_c, Q):
    limit = 1 << max_c
    next_job = deque()
    while Q:
        start, mid, end = Q.popleft()
        if D[start][mid] > 0 and D[mid][end] > 0:
            new_distance = F[start][mid][0] + F[mid][end][0]
            new_capacity = F[start][mid][1] + (1 << mid)
            if new_capacity < limit:
                if F[start][end][0] is None or F[start][end][0] > new_distance:
                    # print('[start : {}, mid : {}, end : {}] {} -> {} (capa : {})'.format(start, mid, end, F[start][end][0], new_distance, new_capacity))
                    F[start][end] = [new_distance, new_capacity]
                    continue
        next_job.append((start, mid, end))

    # print('floyd_warshall(max_c : {}), F : {}'.format(max_c, F))
    return next_job


if __name__ == '__main__':
    N, Q = map(int, input().split())
    distances = [None] * (N+1)
    for i in range(1, N+1):
        temp = [None] * (N+1)
        j = 1
        for d in map(int, input().split()):
            temp[j] = d
            j += 1
        distances[i] = temp
    # print(distances)

    test_cases = [None] * Q
    result_by_C = {}
    for q in range(Q):
        test_cases[q] = tuple(map(int, input().split()))
        C = test_cases[q][0]
        if C not in result_by_C:
            result_by_C[C] = []
        result_by_C[C].append(q)

    F = [[[None, None] for _ in range(N+1)] for _ in range(N+1)]
    F[0] = None
    first_fill(N, distances, F)

    job_queue = generate_floyd_warshall_job_queue(N)

    for curr_c in sorted(result_by_C.keys()):
        job_queue = floyd_warshall(distances, F, curr_c, job_queue)
        for q in result_by_C[curr_c]:
            s, e = test_cases[q][1], test_cases[q][2]
            test_cases[q] = F[s][e][0] if F[s][e][0] is not None else -1

    for r in test_cases:
        print(r)