"""
https://www.acmicpc.net/problem/1991
"""


def traversal_control(M, i, preorder, inorder, postorder):
    preorder.append(i)
    if M[i][0] is not None:
        traversal_control(M, M[i][0], preorder, inorder, postorder)
    inorder.append(i)
    if M[i][1] is not None:
        traversal_control(M, M[i][1], preorder, inorder, postorder)
    postorder.append(i)


if __name__ == '__main__':
    N = int(input())
    tree_map = {}
    for _ in range(N):
        parent, l_child, r_child = map(str, input().split())
        tree_map[parent] = [None, None]
        if l_child != '.':
            tree_map[parent][0] = l_child
        if r_child != '.':
            tree_map[parent][1] = r_child
    # print(tree_map)

    PRE, IN, POST = [], [], []
    traversal_control(tree_map, 'A', PRE, IN, POST)
    print(''.join(PRE))
    print(''.join(IN))
    print(''.join(POST))