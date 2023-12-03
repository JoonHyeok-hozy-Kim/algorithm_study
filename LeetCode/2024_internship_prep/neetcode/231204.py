class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]

            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m
            
            if l+1 == r:
                return nums[r]
        
        return nums[l]