class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = max_sum
        for i in range(1, len(nums)):            
            if curr_sum < 0:
                curr_sum = nums[i]
                max_sum = max(max_sum, curr_sum)
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum += nums[i]
        
        return max(max_sum, curr_sum)
            
                
            