class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i, v in enumerate(nums):
            if v <= 0:
                nums[i] = n+1
        
        for i, v in enumerate(nums):
            a = abs(v) - 1
            if a < n and nums[a] > 0:
                nums[a] *= -1
        
        for i, v in enumerate(nums):
            if v > 0:
                return i+1
        
        return n+1