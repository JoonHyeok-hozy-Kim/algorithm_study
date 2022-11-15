"""
https://www.acmicpc.net/problem/14244
"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    # print(N, M)

    inner_node = 1
    leaf_cnt = 2

    print(0, inner_node)
    leaf_id = 2
    while leaf_cnt < M:
        print(inner_node, leaf_id)
        leaf_id += 1
        leaf_cnt += 1
    next_inner = leaf_id
    while next_inner <= N-1:
        print(inner_node, next_inner)
        inner_node = next_inner
        next_inner = inner_node + 1
