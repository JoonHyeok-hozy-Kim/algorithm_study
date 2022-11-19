"""
https://www.acmicpc.net/problem/2533
"""
import sys
sys.setrecursionlimit(10**6)


def dfs(T, curr=1, prev=None):
    for child in T[curr]:
        if prev is None or prev != child:
            dfs(T, False, child, curr)

    return


if __name__ == '__main__':
    N = int(input())
    tree_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree_list[u].append(v)
        tree_list[v].append(u)
    # print(tree_list)
