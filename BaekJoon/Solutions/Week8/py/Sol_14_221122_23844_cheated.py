"""
https://www.acmicpc.net/problem/23844
"""
import sys
sys.setrecursionlimit(10**4)


def traverse_and_count(T, M, P, i=1, depth=0):
    if depth not in M:
        M[depth] = {}
    M[depth][i] = 1
    # print(M)
    # print(P)
    if (depth+1) not in M:
        M[depth+1] = {}

    for child in T[i]:
        if depth == 0 or (depth > 0 and child not in M[depth-1]):
            P[child] = i
            traverse_and_count(T, M, P, child, depth+1)
            M[depth][i] += M[depth+1][child]


def update_subtree_size(M, P, i, depth, amount):
    # print('In update_subtree_size, i : {}, M : {}'.format(i, M))
    M[depth][i] -= amount
    if P[i] is not None:
        update_subtree_size(M, P, P[i], depth-1, amount)


if __name__ == '__main__':
    N, K = map(int, input().split())
    tree_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree_list[u].append(v)
        tree_list[v].append(u)
    # print(tree_list)

    map_by_depth = {}
    parents = [None] * (N+1)
    traverse_and_count(tree_list, map_by_depth, parents)

    for depth in sorted(map_by_depth.keys(), reverse=True):
        # print('depth : {}, len : {}'.format(depth, len(map_by_depth[depth])))
        while len(map_by_depth[depth]) > K:
            # print('depth : {}, nodes : {}'.format(depth, map_by_depth[depth]))
            min_size_node = min(map_by_depth[depth], key=map_by_depth[depth].get)
            min_subtree_size = map_by_depth[depth][min_size_node]
            # print('min_size_node : {}'.format(min_size_node))
            update_subtree_size(map_by_depth, parents, min_size_node, depth, min_subtree_size)
            del map_by_depth[depth][min_size_node]

    print(map_by_depth[0][1])