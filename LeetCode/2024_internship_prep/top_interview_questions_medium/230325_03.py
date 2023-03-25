class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for n in nums:
            i = bisect_left(dp, n)
            
            if i == len(dp):
                dp.append(n)
            else:
                dp[i] = n
        
        return len(dp)