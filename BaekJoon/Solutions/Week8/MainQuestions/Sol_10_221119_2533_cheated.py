"""
https://www.acmicpc.net/problem/2533
"""
input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**6)


def dfs(T, E, V, i=1, depth=0):
    V[i] = 1
    # print(' '*depth, end="")
    # print('At {}, E : {}'.format(i, E))
    if len(T[i]) == 0:
        E[i][0] = 0
        E[i][1] = 1
    else:
        for linked in T[i]:
            if V[linked] == 0:
                dfs(T, E, V, linked, depth+2)
                E[i][0] += E[linked][1]
                E[i][1] += min(E[linked][0], E[linked][1])
        E[i][1] += 1
    # print(' '*depth, end="")
    # print('At {}, E : {}'.format(i, E))


if __name__ == '__main__':
    N = int(input())
    tree_list = [[] for _ in range(N+1)]
    early_list = [[0, 0] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree_list[u].append(v)
        tree_list[v].append(u)
    # print(tree_list)

    dfs(tree_list, early_list, visited)
    print(min(early_list[1][0], early_list[1][1]))