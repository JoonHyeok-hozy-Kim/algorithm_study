"""
https://www.acmicpc.net/problem/20040
"""


def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    if x == y:
        return
    px, py = find(p, x), find(p, y)
    if px < py:
        p[py] = px
    else:
        p[px] = py


if __name__ == '__main__':
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]

    result = 0
    for m in range(M):
        a, b = map(int, input().split())
        if find(parents, a) == find(parents, b):
            result = m+1
            break
        union(parents, a, b)

    print(result)