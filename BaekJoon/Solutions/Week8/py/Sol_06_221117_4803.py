"""
https://www.acmicpc.net/problem/4803
"""


def count_trees(N, T, V):
    result = 0
    for i in range(1, N+1):
        if V[i] == 0:
            if traverse(T, V, i):
                result += 1
    # print(V)
    return result


def traverse(T, V, curr, prev=None):
    # print('In traverse, curr : {}, prev : {}'.format(curr, prev))
    if V[curr] > 0:
        return False

    V[curr] = 1
    for linked in T[curr]:
        if prev is not None and linked != prev and V[linked] == 0:
            go_on = traverse(T, V, linked, curr)
        elif prev is None and V[linked] == 0:
            go_on = traverse(T, V, linked, curr)
        elif prev is not None and prev == linked:
            go_on = True
        else:
            # print('[PT4] curr : {}, prev : {}, linked : {}'.format(curr, prev, linked))
            V[linked] = 1
            go_on = False

        if not go_on:
            return False

    # if prev is None:
    #     print('At {}, go_on : {}'.format(curr, go_on))
    return True


if __name__ == '__main__':
    test_case_cnt = 0
    result_list = []
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        else:
            test_case_cnt += 1
            tree_list = [[] for _ in range(N+1)]
            visited = [0] * (N+1)
            for _ in range(M):
                x, y = map(int, input().split())
                tree_list[x].append(y)
                tree_list[y].append(x)
            # print('tree_list : {}'.format(tree_list))

            cnt = count_trees(N, tree_list, visited)
            # print('Case {}: '.format(test_case_cnt), end="")
            result_list.append('Case ')
            result_list.append(str(test_case_cnt))
            result_list.append(': ')
            if cnt > 1:
                # print('A forest of {} trees.'.format(cnt))
                result_list.append('A forest of ')
                result_list.append(str(cnt))
                result_list.append(' trees.\n')
            elif cnt == 1:
                # print('There is one tree.')
                result_list.append('There is one tree.\n')
            else:
                # print('No trees.')
                result_list.append('No trees.\n')
    print(''.join(result_list))