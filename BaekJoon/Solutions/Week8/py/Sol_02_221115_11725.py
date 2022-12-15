"""
https://www.acmicpc.net/problem/11725
"""
import sys
sys.setrecursionlimit(100000)


def pre_order_traversal(M, D, i, parent=None):
    # print('In post_order_traversal, i : {}, parent'.format(i, parent))
    if parent is not None:
        dp[i] = parent
    # print('dp : {}'.format(dp))

    for linked in M[i]:
        if D[linked] is None:
            pre_order_traversal(M, D, linked, i)



if __name__ == '__main__':
    N = int(input())
    tree_map = {}
    dp = [None] * (N+1)
    dp[1] = 0
    for _ in range(N-1):
        x, y = map(int, input().split())
        if x not in tree_map:
            tree_map[x] = set()
        tree_map[x].add(y)
        if y not in tree_map:
            tree_map[y] = set()
        tree_map[y].add(x)
    # print(tree_map)

    pre_order_traversal(tree_map, dp, 1)
    # print(dp)

    for i in range(len(dp)):
        if i >= 2:
            print(dp[i])