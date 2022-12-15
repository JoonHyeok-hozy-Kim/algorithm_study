"""
https://www.acmicpc.net/problem/2263
"""
import sys
sys.setrecursionlimit(10**5)


def recursive_solution(I, P, IP, R, i_start=1, i_end=None, p_start=1, p_end=None):
    if i_end is None:
        i_end = len(I)-1
        p_end = len(P)-1

    if i_start > i_end or p_start > p_end:
        return

    parent = P[p_end]
    R.append(parent)
    # print('In recursive_solution, i : {}~{}, p : {}~{}, R : {}'.format(i_start, i_end, p_start, p_end, R))

    if i_start == i_end or p_start == p_end:
        return

    mid = IP[parent]
    l1 = mid-i_start
    l2 = i_end-mid

    recursive_solution(I, P, IP, R, i_start, mid-1, p_start, p_start+l1-1)
    recursive_solution(I, P, IP, R, mid+1, i_end, p_end-l2, p_end-1)


if __name__ == '__main__':
    N = int(input())
    inorder = [-1]
    inorder.extend(list(map(int, input().split())))
    postorder = [-1]
    postorder.extend(list(map(int, input().split())))
    inorder_position = [-1] * (N+1)
    for i in range(1, N+1):
        inorder_position[inorder[i]] = i
    # print(inorder)
    # print(postorder)
    # print(inorder_position)

    result = []
    recursive_solution(inorder, postorder, inorder_position, result)
    print(*result, sep=" ")


"""
4
1 2 3 4
2 4 3 1

5
3 2 5 4 1
2 3 4 1 5
"""