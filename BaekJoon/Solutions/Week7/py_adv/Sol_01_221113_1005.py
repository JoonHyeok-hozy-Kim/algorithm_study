"""
https://www.acmicpc.net/problem/1005
"""
from collections import deque


def dfs(c_map, c_times, i):
    Q = deque()
    Q.append((0, i))
    depth_map = {}
    while Q:
        popped_level, popped = Q.popleft()
        if popped not in depth_map:
            depth_map[popped] = popped_level
        else:
            depth_map[popped] = max(depth_map[popped], popped_level)

        if popped in c_map:
            for prev in c_map[popped]:
                Q.append((popped_level+1, prev))
    # print(depth_map)

    order = []
    for building in depth_map.keys():
        curr_depth = depth_map[building]
        len_order = len(order)
        if len_order < curr_depth+1:
            for _ in range(curr_depth+1-len_order):
                order.append(None)
            order[curr_depth] = c_times[building]
        else:
            order[curr_depth] = max(curr_depth, c_times[building])
    #     print('curr_depth : {}, order : {}'.format(curr_depth, order))
    # print(order)

    print(sum(order))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        const_times = [None] * (N+1)
        idx = 1
        for t in map(int, input().split()):
            const_times[idx] = t
            idx += 1
        const_seq = {}
        for _ in range(K):
            x, y = map(int, input().split())
            if y not in const_seq:
                const_seq[y] = set()
            const_seq[y].add(x)

        W = int(input())

        # print(N, K, W)
        # print(const_times)
        # print(const_seq)

        dfs(const_seq, const_times, W)

"""
1
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
"""