"""
https://www.acmicpc.net/problem/1967
"""
import sys
sys.setrecursionlimit(10**5)


def dfs(T, i, V=None, length=0):
    if V is None:
        V = [0] * len(T)

    # print('dfs, i : {}, length : {}'.format(i, length))
    V[i] = 1
    max_node = i
    max_length = length
    for linked in T[i]:
        if V[linked] == 0:
            temp_node, temp_length = dfs(T, linked, V, length+T[i][linked])
            if temp_length > max_length:
                max_node, max_length = temp_node, temp_length

    # print(' -> i : {}, max_node : {}, max_length : {}'.format(i, max_node, max_length))
    return max_node, max_length


if __name__ == '__main__':
    N = int(input())
    tree_list = [{} for _ in range(N+1)]
    for _ in range(N-1):
        parent, child, weight = map(int, input().split())
        tree_list[parent][child] = weight
        tree_list[child][parent] = weight
    # print(tree_list)

    mn1, ml1 = dfs(tree_list, 1)
    # print(mn1, ml1)

    mn2, ml2 = dfs(tree_list, mn1)
    # print(mn2, ml2)

    print(ml2)