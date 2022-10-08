"""
12865. 평범한 배낭
https://www.acmicpc.net/problem/12865
"""

def recursive_trial(I, K, i=0, w=0, v=0):
    if i == len(I):
        return v

    # print('i : {}, w : {}, v : {}'.format(i, w, v))
    if w+I[i][0] > K:
        v1 = v
    else:
        v1 = recursive_trial(I, K, i+1, w+I[i][0], v+I[i][1])

    v2 = recursive_trial(I, K, i+1, w, v)

    if v1 is None:
        return v2
    elif v2 is None:
        return v1
    else:
        return max(v1, v2)


def knapsack_solution(N, K, I):
    stuff = [[0, 0]]
    stuff.extend(I)
    knapsack = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            w = stuff[i][0]
            v = stuff[i][1]

            if j < w:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])

    # for k in knapsack:
    #     print(k)

    print(knapsack[-1][-1])


if __name__ == '__main__':
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    # print(items)

    # result = recursive_trial(items, K)
    # print(result)

    knapsack_solution(N, K, items)