class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [None for _ in range(len(nums))]
        result[0] = 1

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        right = nums[-1]
        for j in range(len(nums)-2, -1, -1):
            result[j] *= right
            right *= nums[j]
        
        return result