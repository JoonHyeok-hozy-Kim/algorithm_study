class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == 0:
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        
        for i, n in enumerate(s):
            if n == '0':
                if s[i-1] not in '12':
                    return 0
            else:
                dp[i+1] += dp[i]
                    
            if n == '1' and i < len(s)-1:
                dp[i+2] += dp[i]
            elif n == '2' and i < len(s)-1 and s[i+1] in '0123456':
                dp[i+2] += dp[i]
        
        return dp[-1]