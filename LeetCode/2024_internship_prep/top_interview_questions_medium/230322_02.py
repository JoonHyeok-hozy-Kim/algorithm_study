class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        
        def target_check(i, prev=True):
            if nums[i] == target:
                if prev:
                    if i == 0 or nums[i-1] != target:
                        return True
                else:
                    if i == len(nums)-1 or nums[i+1] != target:
                        return True                    
            return False
        
        lower_bound = -1
        upper_bound = -1
                
        # Get lower bound.
        start, end = 0, len(nums)
        while start < end-1:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                if target_check(mid, True):
                    lower_bound = mid
                    break
                else:
                    end = mid
                    
        if lower_bound == -1:
            if nums[start] == target:
                lower_bound = start
            elif end < len(nums) and nums[end] == target:
                lower_bound = end
            else:
                return [-1, -1]
            
        # Get upper bound.
        start, end = lower_bound, len(nums)
        while start < end-1:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                if target_check(mid, False):
                    upper_bound = mid
                    break
                else:
                    start = mid
        
        if upper_bound == -1:
            if end < len(nums) and nums[end] == target:
                upper_bound = end
            elif nums[start] == target:
                upper_bound = start
        
        return [lower_bound, upper_bound]