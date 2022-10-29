"""
https://www.acmicpc.net/problem/1463
"""


if __name__ == '__main__':
    N = int(input())

    dp = [None] * (N+1)
    dp[0] = dp[1] = 0

    for i in range(2, N+1):
        if dp[i] is None:
            candidates = []
            if i >= 3 and i%3 == 0:
                candidates.append(dp[i//3])
            if i >= 2 and i%2 == 0:
                candidates.append(dp[i//2])
            if i >= 1:
                candidates.append(dp[i-1])
            dp[i] = min(candidates) + 1

            # print(dp)

    print(dp[-1])