"""
https://www.acmicpc.net/problem/1949
"""
import sys
sys.setrecursionlimit(10**4)


def recursive_solution(P, T, E, i):
    E[i][0] = 0
    E[i][1] = P[i]
    for linked in T[i]:
        if E[linked][0] is None:
            recursive_solution(P, T, E, linked)
            E[i][0] += max(E[linked][0], E[linked][1])
            E[i][1] += E[linked][0]
    # print(E)


if __name__ == '__main__':
    N = int(input())
    population = [None]
    population.extend(list(map(int, input().split())))
    tree_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree_list[u].append(v)
        tree_list[v].append(u)

    excellence = [[None, None] for _ in range(N+1)]
    recursive_solution(population, tree_list, excellence, 1)
    print(max(excellence[1][0], excellence[1][1]))