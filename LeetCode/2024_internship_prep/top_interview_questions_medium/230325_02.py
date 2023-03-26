class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [0] * (amount + 1)
        for c in coins:
            if c < len(dp):
                dp[c] = 1
        
        for i in range(1, len(dp)):
            for c in coins:
                if i-c > 0 and dp[i-c] > 0:
                    temp = dp[i-c] + 1
                    if dp[i] == 0:
                        dp[i] = temp
                    else:
                        dp[i] = min(dp[i], temp)
        
        if dp[-1] > 0:
            return dp[-1]
        else:
            return -1