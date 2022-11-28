"""
https://www.acmicpc.net/problem/24888
"""
from heapq import heappush, heappop
from math import inf
from copy import deepcopy
import sys
sys.setrecursionlimit(2*(10**5))


def dijkstra(N, E, P):
    dp = [[inf, None]] * (N+1)
    dp[1][0] = 0
    dp[1][1] = {1} if 1 in P else {}
    heap = []
    heappush(heap, (0, dp[1][1], 1))
    while heap:
        print('dp : {}'.format(dp))
        popped_distance, popped_set, popped = heappop(heap)

        if E[popped] is not None:
            for linked in E[popped]:
                new_distance = popped_distance + E[popped][linked]

                if dp[linked][0] < new_distance:
                    continue
                else:
                    set_copy = deepcopy(popped_set)
                    if linked in P:
                        set_copy.add(linked)

                    if dp[linked][0] > new_distance:
                        dp[linked] = [new_distance, set_copy]
                    elif len(dp[linked][1]) < set_copy:
                        dp[linked][1] = set_copy
                    heappush(heap, (new_distance, dp[linked][1], linked))

    return dp


def back_track(E, P, D, i, result=[]):
    result.append(i)
    if i in D[i][1]:
        D[i][1].remove(i)

    if i == 1:
        if len(D[i][1]) == 0:
            return True, result
        else:
            result.pop()
            D[i][1].add(i)
            return False, None

    if E[i] is not None:
        for j in E[i]:
            if D[i][0] > D[j][0]:
                go_on, temp = back_track(E, P, D, j, result)
                if go_on:
                    return True, temp

    result.pop()
    D[i][1].add(i)
    return False, None


if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = [None] * (N+1)
    for _ in range(M):
        u, v, w = map(int, input().split())
        if edges[u] is None:
            edges[u] = {}
        edges[u][v] = w

        if edges[v] is None:
            edges[v] = {}
        edges[v][u] = w

    parts_spread = set()
    cnt = 1
    added_cnt = 0
    for i in map(int, input().split()):
        if i == 1:
            parts_spread.add(cnt)
            added_cnt += 1
        cnt += 1
    # print('added_cnt : {}, parts_spread : {}'.format(added_cnt, parts_spread))

    DP = dijkstra(N, edges, parts_spread)
    print(DP)
    if DP[N][1] is None or len(DP[N][1]) < added_cnt:
        print(-1)
    else:
        finale, result = back_track(edges, parts_spread, DP, N)
        if finale:
            print(len(result))
            print(*reversed(result), sep=" ")
        else:
            print(-1)