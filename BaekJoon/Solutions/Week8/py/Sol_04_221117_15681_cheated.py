"""
https://www.acmicpc.net/problem/15681
"""
import sys
sys.setrecursionlimit(10**5)


def postorder_traversal(L, i, D):
    D[i] = 1
    for child in L[i]:
        if D[child] == 0:
            D[i] += postorder_traversal(L, child, D)

    # print('postorder_traversal, i : {}, D : {}'.format(i, D))
    return D[i]


if __name__ == '__main__':
    N, R, Q = map(int, input().split())
    dp = [0] * (N+1)

    tree_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        x, y = map(int, input().split())
        tree_list[x].append(y)
        tree_list[y].append(x)
    # print(tree_list)

    postorder_traversal(tree_list, R, dp)
    queries = [None] * Q
    for j in range(Q):
        queries[len(queries)-1-j] = int(input())

    while len(queries) > 0:
        print(dp[queries.pop()])
