class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dp = [0] * ((10**4) * 2 + 1)
        max_idx = 0
        
        for i, v in enumerate(nums):
            max_idx = max(max_idx, v + (10**4))
            dp[v + (10**4)] += 1
            
        for i in range(1, k):
            if dp[max_idx] > 0:
                dp[max_idx] -= 1
                k -= 1
            
            while dp[max_idx] == 0:
                max_idx -= 1
                
        
        return max_idx - 10**4