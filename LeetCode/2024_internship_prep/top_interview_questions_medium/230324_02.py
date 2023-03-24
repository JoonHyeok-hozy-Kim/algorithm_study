class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        
        if curr == 0 and len(nums) > 1:
            return False
        
        for i, v in enumerate(nums):
            if v == len(nums) -1 :
                return True
            
            curr = max(curr-1, v)
            if curr <= 0 and i != len(nums)-1:
                return False
        
        return True