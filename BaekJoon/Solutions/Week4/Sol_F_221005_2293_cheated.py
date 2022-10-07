"""
2293. 동전 1
https://www.acmicpc.net/problem/2293
"""


if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = []
    for i in range(N):
        coins.append(int(input()))
    # coins.sort()
    # print(coins)

    dp = [0] * (K+1)

    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], K+1):
            dp[j] = dp[j] + dp[j - coins[i]]
    print(dp[-1])

