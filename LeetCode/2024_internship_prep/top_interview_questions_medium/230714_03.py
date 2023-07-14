class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        while left < right:
            mid = (left + right) // 2
            if mid == 0 or mid == len(nums):
                return mid
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            else:
                if nums[mid-1] <= nums[mid+1]:
                    if mid == left:
                        return right
                    left = mid
                else:
                    right = mid
        return left