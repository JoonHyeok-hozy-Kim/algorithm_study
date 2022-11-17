"""
https://www.acmicpc.net/problem/5639
"""
import sys
sys.setrecursionlimit(10**4)


def generate_tree(T, I, i=0, j=1, S=[]):
    if j == len(I):
        return

    if I[i] > I[j]:
        S.append(i)
        T[i][0] = j
        j = generate_tree(T, I, j, j+1, S)
        if j is None:
            return

    if len(S) > 0 and S[-1] == i:
        S.pop()

    if I[i] < I[j]:
        if len(S) == 0 or I[j] < I[S[-1]]:
            T[i][1] = j
            j = generate_tree(T, I, j, j+1, S)

    # print('i : {}, j : {}, S : {}, T : {}'.format(i, j, S, T))
    return j


def postorder_traversal(T, I, R, i=0):
    # print('In postorder_traversal, i : {}'.format(i))
    if T[i][0] is not None:
        postorder_traversal(T, I, R, T[i][0])
    if T[i][1] is not None:
        postorder_traversal(T, I, R, T[i][1])
    R.append(I[i])
    # print(R)


if __name__ == '__main__':
    inputs = []
    while True:
        try:
            txt = input()
            inputs.append(int(txt))
            # print(inputs)
        except ValueError:
            break
        except EOFError:
            break
    # print(inputs)

    tree_list = [[None, None] for _ in range(len(inputs))]
    generate_tree(tree_list, inputs)
    # print(tree_list)

    result_list = []
    postorder_traversal(tree_list, inputs, result_list)
    for val in result_list:
        print(val)


"""
10
5
6
7
8
15
14
13
12
"""