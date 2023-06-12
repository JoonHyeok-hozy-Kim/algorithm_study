class Solution:
    def numSquares(self, n: int) -> int:
        dp = [None] * (n+1)
        dp[0] = 0
        m = 1
        while m ** 2 <= n:
            m += 1
        
        for i in range(m-1, 0, -1):
            j = i ** 2
            for k in range(j, n+1, j):
                dp[k] = min(dp[k], dp[k-j]+1) if dp[k] is not None else dp[k-j]+1
        
        return dp[-1]
                