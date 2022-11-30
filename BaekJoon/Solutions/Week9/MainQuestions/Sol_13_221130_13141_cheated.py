"""
https://www.acmicpc.net/problem/13141
"""
from math import inf


def floyd_warshall(L):
    for mid in range(1, N+1):
        for start in range(1, N+1):
            if start == mid:
                continue
            for end in range(1, N+1):
                if start == end or mid == end:
                    continue
                L[start][end] = min(L[start][end], L[start][mid] + L[mid][end])


if __name__ == '__main__':
    N, M = map(int, input().split())
    longests = [[None] * (N+1) for _ in range(N+1)]
    distances = [[inf] * (N+1) for _ in range(N+1)]

    for m in range(M):
        s, e, l = map(int, input().split())
        if longests[s][e] is None or longests[s][e] < l:
            longests[s][e] = l
        if distances[s][e] is None or distances[s][e] > l:
            distances[s][e] = l
        longests[e][s], distances[e][s] = longests[s][e], distances[s][e]

    print('distances : {}'.format(distances))
    floyd_warshall(distances)
    print('distances : {}'.format(distances))