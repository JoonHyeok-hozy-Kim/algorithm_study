"""
https://www.acmicpc.net/problem/1717
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(P, x):
    if P[x] == x:
        return x
    P[x] = find(P, P[x])
    return P[x]


def union(P, x, y):
    if x == y:
        return
    px, py = find(P, x), find(P, y)
    if px > py:
        P[py] = px
    else:
        P[px] = py


if __name__ == '__main__':
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]

    for _ in range(M):
        opr, a, b = map(int, input().split())
        if opr == 0:
            union(parents, a, b)
        else:
            print('YES') if find(parents, a) == find(parents, b) else print('NO')