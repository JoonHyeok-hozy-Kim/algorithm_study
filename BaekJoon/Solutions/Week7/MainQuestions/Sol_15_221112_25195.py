"""
https://www.acmicpc.net/problem/25195
"""
from collections import deque


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = {}
    for _ in range(M):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    # print(graph)

    S = int(input())
    undercover = [None] * (N+1)
    for s in map(int, input().split()):
        undercover[s] = 1
    # print(undercover)

    S = list()
    S.append(1)
    success = False
    while S:
        popped = S.pop()
        if undercover[popped] is None:
            if popped not in graph:
                success = True
                break
            else:
                for j in graph[popped]:
                    S.append(j)

    if success:
        print("yes")
    else:
        print("Yes")