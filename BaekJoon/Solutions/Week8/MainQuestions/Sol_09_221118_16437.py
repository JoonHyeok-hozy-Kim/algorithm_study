"""
https://www.acmicpc.net/problem/16437
"""
input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(150000)


def post_order_traversal(T, i=1):
    # print(i)
    for child in T[i][1]:
        post_order_traversal(T, child)
        T[i][0] += T[child][0]

    if T[i][0] < 0:
        T[i][0] = 0


if __name__ == '__main__':
    N = int(input())
    tree_list = [[0, []] for _ in range(N+1)]
    for i in range(N-1):
        idx = i+2
        w_or_s, num, connected = map(str, input().split())
        tree_list[idx][0] = int(num)
        if w_or_s == 'W':
            tree_list[idx][0] *= -1
        tree_list[int(connected)][1].append(idx)
    # print('tree_list : {}'.format(tree_list))
    # print('islands : {}'.format(islands))

    post_order_traversal(tree_list)
    print(tree_list[1][0])