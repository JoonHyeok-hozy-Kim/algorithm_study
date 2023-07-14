class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        if nums[left] > nums[right]:
            mid = left
            while mid < right and nums[mid] < nums[mid+1]:
                mid += 1
            
            if target > nums[mid]:
                return -1
            else:
                if target <= nums[right]:
                    left = mid+1
                else:
                    right = mid
        
        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            else:
                if left == mid:
                    break
                left = mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1