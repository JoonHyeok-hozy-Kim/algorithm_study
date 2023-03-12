def triple_step(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        if i + 1 < n:
            dp[i+1] += dp[i]
        if i + 2 < n:
            dp[i+2] += dp[i]
        if i + 3 < n:
            dp[i+3] += dp[i]
    return dp[-1]

if __name__ == '__main__':
    for i in range(1, 10):
        print(triple_step(i))