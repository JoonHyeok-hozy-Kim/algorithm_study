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
        elif n > 0:
            pos += n

    if S < neg or S > pos:
        print(0)
    else:
        dp = [0] * (pos-neg+1)
        for n in series:
            copy_dp = deepcopy(dp)
            for i in range(len(dp)):
                if i + n == len(dp):
                    break
                if copy_dp[i] != 0:
                    dp[i+n] += copy_dp[i]
            dp[n-neg] += 1
            # print(dp)
        print(dp[S - neg])