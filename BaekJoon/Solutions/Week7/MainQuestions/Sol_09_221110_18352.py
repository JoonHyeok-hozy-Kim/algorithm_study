"""
https://www.acmicpc.net/problem/18352
"""
from collections import deque


if __name__ == '__main__':
    N, M, K, X = map(int, input().split())
    edges = {}
    for _ in range(M):
        x, y = map(int, input().split())
        if x not in edges:
            edges[x] = set()
        edges[x].add(y)

    dp = [None] * (N+1)
    dp[X] = 0
    Q = deque()
    Q.append(X)
    result = []
    while Q:
        popped = Q.popleft()
        if popped in edges:
            for Y in edges[popped]:
                if dp[Y] is None or dp[Y] > dp[popped] + 1:
                    dp[Y] = dp[popped] + 1
                    if dp[Y] == K:
                        result.append(Y)
                    Q.append(Y)
            # print(dp)

    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        print(*result, sep="\n")