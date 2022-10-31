"""
https://www.acmicpc.net/problem/2293
"""


if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    # print(coins)

    dp = [0] * (K+1)

    for i in range(N):
        if coins[i] < len(dp):
            dp[coins[i]] += 1
        for j in range(len(dp)-1):
            if j + coins[i] < len(dp):
                dp[j+coins[i]] += dp[j]
        # print(dp)

    print(dp[-1])