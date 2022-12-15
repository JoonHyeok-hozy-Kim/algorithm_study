"""
https://www.acmicpc.net/problem/2533
"""
input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**6)


def recursive_trial(T, E, i, total_cnt=None):
    all_early_flag = True
    for linked in T[i]:
        if E[linked] == 0:
            all_early_flag = False

    # print('At {}, E : {}'.format(i, E))

    min_early_cnt = None
    if all_early_flag:
        temp_early_cnt = 0
        for linked in T[i]:
            if E[linked] is None:
                E[i] = 0
                temp_early_cnt += recursive_trial(T, E, linked)
        min_early_cnt = min(min_early_cnt, temp_early_cnt) if min_early_cnt is not None else temp_early_cnt

    temp_early_cnt = 1
    for linked in T[i]:
        if E[linked] is None:
            E[i] = 1
            temp_early_cnt += recursive_trial(T, E, linked)
            if min_early_cnt is not None and min_early_cnt < temp_early_cnt:
                temp_early_cnt = None
                break

    if temp_early_cnt is not None:
        min_early_cnt = min(min_early_cnt, temp_early_cnt) if min_early_cnt is not None else temp_early_cnt

    E[i] = None
    return min_early_cnt


if __name__ == '__main__':
    N = int(input())
    tree_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree_list[u].append(v)
        tree_list[v].append(u)
    # print(tree_list)

    early_list = [None] * (N+1)
    result = recursive_trial(tree_list, early_list, 1)
    print(result)