"""
https://www.acmicpc.net/problem/2805
"""
from bisect import bisect_right


def counting_from_top_solution(N, M, T):
    T.sort(reverse=True)
    # print(trees)

    idx = 0
    height_cnt = T[0]
    while idx < N:
        if idx < N-1 and T[idx] == T[idx+1]:
            while idx < N-1 and T[idx] == T[idx+1]:
                idx += 1
        curr_height = T[idx]
        next_height = T[idx+1] if idx < N-1 else 0
        if (idx+1)*(curr_height-next_height) >= M:
            # print('M : {}, idx+1 : {}'.format(M, idx+1))
            height_cnt -= (M-1) // (idx+1)
            break
        else:
            height_cnt -= curr_height-next_height
            M -= (idx+1)*(curr_height-next_height)
        # print('height_cnt : {}, M : {}'.format(height_cnt, M))
        idx += 1
    return height_cnt-1


if __name__ == '__main__':
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    print(counting_from_top_solution(N, M, trees))

"""
10 18
10 9 9 9 7 7 7 7 7 6
"""