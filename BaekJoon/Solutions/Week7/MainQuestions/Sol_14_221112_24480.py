"""
https://www.acmicpc.net/problem/24480
"""


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

    S = list()
    S.append(R)
    cnt = 1
    while len(S) > 0:
        popped = S.pop()
        if visited[popped] == 0:
            visited[popped] = cnt
            cnt += 1
            if popped in graph:
                graph[popped].sort()
                for j in graph[popped]:
                    S.append(j)

    for i in range(1, N+1):
        print(visited[i])