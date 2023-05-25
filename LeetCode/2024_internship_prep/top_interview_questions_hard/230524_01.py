class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0] * n
        S = []
        
        for i in range(n-1, -1, -1):
            if len(S) == 0:
                S.append(nums[i])
            else:
                j = bisect_left(S, nums[i])
                dp[i] = j
                S.insert(j, nums[i])
        
        return dp