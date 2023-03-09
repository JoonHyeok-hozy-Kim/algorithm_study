class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1
            
            while i < j < k:
                if val + nums[j] + nums[k] == 0:
                    result.append([val, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                    while k >= 0 and nums[k] == nums[k+1]:
                        k -= 1
                elif val + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
                    
        return result