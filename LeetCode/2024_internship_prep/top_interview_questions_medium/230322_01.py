class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def is_decreasing(i):
            if i == len(nums)-1:
                if nums[i-1] > nums[i]:
                    return True
                else:
                    return False
            
            if nums[i] > nums[i+1]:
                return True
            else:
                return False
        
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums)
        mid = None
        while True:
            mid = (left + right) // 2
            if mid == left:
                break
                
            if is_decreasing(mid):
                right = mid
            else:
                left = mid
            
        if right == len(nums) or nums[left] > nums[right]:
            return left
        else:
            return right
            