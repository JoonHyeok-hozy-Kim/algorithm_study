"""
1208. 부분수열의 합 2
https://www.acmicpc.net/problem/1208
"""
from collections import deque


if __name__ == '__main__':
    N, S = map(int, input().split())
    series = list(map(int, input().split()))
    # print(series)

    neg_cnt = 0
    pos_cnt = 0
    for i in range(N):
        if series[i] < 0:
            neg_cnt += series[i]
        else:
            pos_cnt += series[i]

    if S > 0:
        pos_cnt = max(pos_cnt, S)
    else:
        neg_cnt = min(neg_cnt, S)

    dp = [0] * (pos_cnt - neg_cnt + 2)
    zero_idx = 1 - neg_cnt

    for i in range(N):
        temp_list = []
        for j in range(len(dp)):
            if dp[j] > 0:
                temp_list.append((j + series[i], dp[j]))

            if j == zero_idx + series[i]:
                dp[zero_idx + series[i]] += 1

        for t in temp_list:
            # print('t : {}'.format(t))
            dp[t[0]] += t[1]
        # print(series[i], dp)

    print(dp[zero_idx + S])




