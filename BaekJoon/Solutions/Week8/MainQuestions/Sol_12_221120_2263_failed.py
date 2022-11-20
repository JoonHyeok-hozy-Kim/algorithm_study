"""
https://www.acmicpc.net/problem/2263
"""
input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**6)


def generate_tree_by_inorder(N, I, P, i=0, T=None, curr_top=None):
    if T is None:
        T = [[None, None, None] for _ in range(N+1)]
        curr_top = I[i]

    if i == N-1:
        # print('top : {}, T : {}'.format(curr_top, T))
        postorder_generated = []
        get_post_order(T, curr_top, postorder_generated)
        # print('postorder_generated : {}'.format(postorder_generated))
        if compare_list(postorder_generated, P):
            # print('Final T : {}'.format(T))
            return T, curr_top
        else:
            return None, None

    else:
        # print('Case 1. parent : {} / r_child : {}'.format(I[i], I[i+1]))
        T[I[i]][2] = I[i+1]
        T[I[i+1]][0] = I[i]
        temp, temp_top = generate_tree_by_inorder(N, I, P, i+1, T, curr_top)
        if temp is not None:
            return temp, temp_top
        T[I[i]][2] = None
        T[I[i+1]][0] = None

        if T[I[i]][0] is None:
            # print('Case 2-1. l_child : {} / parent : {}'.format(I[i], I[i+1]))
            T[I[i]][0] = I[i+1]
            T[I[i+1]][1] = I[i]
            temp, temp_top = generate_tree_by_inorder(N, I, P, i+1, T, I[i+1])
            if temp is not None:
                return temp, temp_top
            T[I[i]][0] = None
            T[I[i+1]][1] = None

        else:
            # print('Case 2-2. l_child : {} / parent : {}'.format(I[i], I[i+1]))
            i_parent = T[I[i]][0]
            T[I[i]][0] = I[i+1]
            T[I[i+1]][1] = I[i]
            T[I[i+1]][0] = i_parent
            T[i_parent][2] = I[i+1]
            temp, temp_top = generate_tree_by_inorder(N, I, P, i+1, T, curr_top)
            if temp is not None:
                return temp, temp_top
            T[I[i]][0] = i_parent
            T[I[i+1]][1] = None
            T[I[i+1]][0] = None
            T[i_parent][2] = I[i]

            # print('Case 2-3. {} going top'.format(I[i+1]))
            j = T[I[i]][0]
            while T[j][0] is not None:
                j = T[j][0]
            T[j][0] = I[i+1]
            T[I[i+1]][1] = j
            temp, temp_top = generate_tree_by_inorder(N, I, P, i+1, T, I[i+1])
            if temp is not None:
                return temp, temp_top
            T[j][0] = None
            T[I[i+1]][1] = None

        return None, None


def get_post_order(T, i, R):
    if T[i][1] is not None:
        get_post_order(T, T[i][1], R)
    if T[i][2] is not None:
        get_post_order(T, T[i][2], R)
    R.append(i)


def compare_list(A, B):
    # print('In compare_list : {} vs {}'.format(A, B))
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


def preorder(T, i):
    print(i, end=" ")
    if T[i][1] is not None:
        preorder(T, T[i][1])
    if T[i][2] is not None:
        preorder(T, T[i][2])


if __name__ == '__main__':
    N = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    # print(inorder)
    # print(postorder)

    result_tree, result_top = generate_tree_by_inorder(N, inorder, postorder)
    # print(result_top, result_tree)
    preorder(result_tree, result_top)




"""
4
1 2 3 4
1 2 3 4
"""