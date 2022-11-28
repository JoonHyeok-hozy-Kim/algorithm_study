"""
https://www.acmicpc.net/problem/24888
"""
from heapq import heappush, heappop
from collections import deque
from math import inf
import sys
sys.setrecursionlimit(2*(10**5)+1)
input = __import__('sys').stdin.readline


def dijkstra(N, E, P):
    distances = [[inf, 0]] * (N+1)
    distances[1] = [0, P[1]]
    heap = []
    heappush(heap, (0, P[1], 1))
    final_min_length = None
    while heap:
        popped_distance, popped_cnt, popped = heappop(heap)

        if popped == N:
            if final_min_length is None or final_min_length > popped_distance:
                final_min_length = popped_distance

        if final_min_length is not None and popped_distance > final_min_length:
            continue

        if final_min_length is None or final_min_length >= popped_distance:
            if E[popped] is not None:
                for linked in E[popped]:
                    new_distance = E[popped][linked] + popped_distance
                    new_cnt = popped_cnt + P[linked]
                    if final_min_length is None or final_min_length >= new_distance:
                        if distances[linked][0] > new_distance:
                            distances[linked] = [new_distance, new_cnt]
                        elif distances[linked][0] == new_distance and distances[linked][1] < new_cnt:
                            distances[linked][1] = new_cnt
                        else:
                            continue
                        heappush(heap, (new_distance, new_cnt, linked))

    return distances


def back_track(E, D, P, i, answer_cnt, contain_cnt=0, path=None):
    if path is None:
        path = deque()

    # print('i : {}, answer_cnt : {}, contain_cnt : {}, path : {}'.format(i, answer_cnt, contain_cnt, path))
    if i == 1:
        if contain_cnt + P[1] == answer_cnt:
            path.appendleft(i)
            return True, path
        else:
            return False, None

    path.appendleft(i)
    for j in E[i]:
        if D[i][0] == D[j][0] + E[i][j]:
            if D[i][1] == D[j][1] + P[i]:
                go_on, temp = back_track(E, D, P, j, answer_cnt, contain_cnt+P[i], path)
                if go_on:
                    return True, temp

    path.popleft()
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

    parts_spread = [None] * (N+1)
    idx = 1
    note_cnt = 0
    for i in map(int, input().split()):
        parts_spread[idx] = i
        if i == 1:
            note_cnt += 1
        idx += 1

    distances = dijkstra(N, edges, parts_spread)
    # print(distances)

    if distances[N][1] != note_cnt:
        print(-1)
    else:
        finale, result = back_track(edges, distances, parts_spread, N, note_cnt)
        if finale:
            print(len(result))
            print(*result, sep=" ")
        else:
            print(-1)


"""
6 6
1 2 1
2 3 1
3 4 1
4 6 1
1 5 2
5 6 2
1 0 1 1 1 1

6 6
1 2 1
2 3 1
3 4 1
4 6 1
1 5 2
5 6 2
1 0 1 1 0 1

6 6
1 2 1
2 3 1
3 4 1
4 6 1
1 5 2
5 6 2
1 0 0 0 1 1
"""