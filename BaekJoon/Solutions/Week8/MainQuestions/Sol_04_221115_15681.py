"""
https://www.acmicpc.net/problem/15681
"""
from collections import deque
import sys
sys.setrecursionlimit(100000)


def postorder_traversal(M, D, i):
    D[i] = 0
    subtree_size = 1
    for child in M[i]:
        if D[child] is None:
            D[child] = 0
            subtree_size += postorder_traversal(M, D, child)
    D[i] = subtree_size
    return subtree_size


def postorder_traversal_break_ver(M, D, i, Qu):
    if len(Qu) == 0:
        return None

    if D[i] is None:
        D[i] = 0

    subtree_size = 1
    if i in M:
        for child in M[i]:
            if D[child] is None:
                temp = postorder_traversal_break_ver(M, D, child, Qu)
                if temp is None:
                    return None
                else:
                    subtree_size += temp
            elif D[child] > 0:
                subtree_size += D[child]
    D[i] = subtree_size

    if len(Qu) == 0:
        return None
    else:
        while len(Qu) > 0 and D[Qu[0]] is not None and D[Qu[0]] > 0:
            print(D[Qu[0]])
            Qu.popleft()

    # print('In postorder_traversal, i : {}, dp : {}'.format(i, dp))
    return subtree_size


def postorder_traversal_break_ver_q_cnt(M, D, i, Q, curr_q, q_cnt):
    print('In postorder_traversal_break_ver_q_cnt, i :{}, curr_q : {}, q_cnt : {}'.format(i, curr_q, q_cnt))
    if q_cnt == Q:
        return None, None

    if D[i] is None:
        D[i] = 0

    subtree_size = 1
    if i in M:
        for child in M[i]:
            if D[child] is None:
                temp, curr_q = postorder_traversal_break_ver_q_cnt(M, D, child, Q, curr_q, q_cnt)
                if temp is None:
                    return None, None
                else:
                    subtree_size += temp
            elif D[child] > 0:
                subtree_size += D[child]
    D[i] = subtree_size

    if D[curr_q] > 0:
        print(D[curr_q])
        q_cnt += 1
        if q_cnt == Q:
            return None, None
        else:
            curr_q = int(input())

    return subtree_size, curr_q


if __name__ == '__main__':
    N, R, Q = map(int, input().split())
    tree_map = {}
    dp = [None] * (N+1)
    for _ in range(N-1):
        U, V = map(int, input().split())
        if U not in tree_map:
            tree_map[U] = set()
        tree_map[U].add(V)
        if V not in tree_map:
            tree_map[V] = set()
        tree_map[V].add(U)
    # print(tree_map)

    # queries = deque()
    # for _ in range(Q):
    #     queries.append(int(input()))

    # postorder_traversal_break_ver(tree_map, dp, R, queries)

    # postorder_traversal(tree_map, dp, R)
    # for _ in range(Q):
    #     print(dp[int(input())])

    curr_q = int(input())
    postorder_traversal_break_ver_q_cnt(tree_map, dp, R, Q, curr_q, 0)