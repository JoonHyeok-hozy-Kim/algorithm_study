"""
https://www.acmicpc.net/problem/24444
"""
from collections import deque


if __name__ == '__main__':
    N, M, R = map(int, input().split())
    visited = [0] * (N+1)
    graph = {}
    for _ in range(M):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        if v not in graph:
            graph[v] = []
        graph[v].append(u)
    # print(graph)

    Q = deque()
    Q.append(R)
    cnt = 1
    while Q:
        popped = Q.popleft()
        if visited[popped] == 0:
            visited[popped] = cnt
            cnt += 1
            graph[popped].sort()
            for j in graph[popped]:
                Q.append(j)
    for i in range(1, N+1):
        print(visited[i])