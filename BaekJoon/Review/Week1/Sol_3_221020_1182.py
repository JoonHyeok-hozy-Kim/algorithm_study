"""
https://www.acmicpc.net/problem/1182
"""
from copy import deepcopy

if __name__ == '__main__':
    N, S = map(int, input().split())
    series = list(map(int, input().split()))
    # print(N, S, series)

    neg, pos = 0, 0
    for n in series:
        if n < 0:
            neg += n
        else:
            pos += n

    dp = [0] * (pos-neg+1)
    for n in series:
        copy_dp = deepcopy(dp)
        for i in range(len(dp)):
            if copy_dp[i] != 0 and i + n < len(copy_dp):
                dp[i+n] += copy_dp[i]
        dp[n-neg] += 1
        # print(dp)
    print(dp[S - neg])