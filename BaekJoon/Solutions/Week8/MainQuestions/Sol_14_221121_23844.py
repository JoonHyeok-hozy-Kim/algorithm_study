"""
https://www.acmicpc.net/problem/23844
"""
from collections import deque


def calculate_thickness(T, max_thickness):
    Q = deque()
    Q.append([1, 0])
    curr_depth = 0
    curr_thickness = 0
    while Q:
        # print('curr_depth : {}, curr_thickness : {}'.format(curr_depth, curr_thickness))
        popped, depth = Q.popleft()
        if depth == curr_depth:
            curr_thickness += 1
            if curr_thickness > max_thickness:
                return depth            
            for child in T[popped]:
                Q.append([child, depth+1])

        else:
            curr_depth = depth
            curr_thickness = 1
            if curr_thickness > max_thickness:
                return depth



if __name__ == '__main__':
    N, K = map(int, input().split())
    tree_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree_list[u].append(v)
    # print(tree_list)

    validated_depth = calculate_thickness(tree_list, K)
    print(validated_depth)