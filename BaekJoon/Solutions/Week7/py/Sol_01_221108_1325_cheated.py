"""
https://www.acmicpc.net/problem/1325
"""
import sys
sys.setrecursionlimit(10000)
from collections import deque


def bfs(E, N, start):
    Q = deque()
    record = [None] * (N+1)
    record[start] = 1
    Q.append(start)
    cnt = 1
    while len(Q) > 0:
        popped = Q.popleft()
        if popped in E:
            for c in E[popped]:
                if record[c] is None:
                    record[c] = 1
                    Q.append(c)
                    cnt += 1
    return cnt


def dfs(E, N, i, record=None):
    if record is None:
        record = [None] * (N+1)

    if record[i] is not None:
        return 0

    else:
        record[i] = 1
        cnt = 1
        if i in E:
            for c in E[i]:
                cnt += dfs(E, N, c, record)
        return cnt


if __name__ == '__main__':
    N, M = map(int, input().split())
    edge_map = {}
    vertices_map = {}

    for _ in range(M):
        v_to, v_from = map(int, input().split())
        if v_from not in edge_map:
            edge_map[v_from] = []
        edge_map[v_from].append(v_to)
        vertices_map[v_from] = True
    # print(edge_map)

    max_cnt = 0
    result_list = []
    for v in vertices_map:
        # temp_cnt = bfs(edge_map, N, v)
        temp_cnt = dfs(edge_map, N, v)
        if temp_cnt > max_cnt:
            result_list = [v]
            max_cnt = temp_cnt
        elif temp_cnt == max_cnt:
            result_list.append(v)

    result_list.sort()
    print(*result_list, sep=" ")

"""
3 3
1 2
2 3 
3 1

6 5
1 2
2 3
3 1
4 5
5 6
"""