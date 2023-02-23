class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[-1] = 1
        idx = n
        
        while idx > 0:
            if idx-1 >= 0:
                dp[idx-1] += dp[idx]
            if idx-2 >= 0:
                dp[idx-2] += dp[idx]
            idx -= 1
        
        return dp[0]
        