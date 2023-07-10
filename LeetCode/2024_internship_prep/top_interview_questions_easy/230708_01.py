class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v is None:
                continue
                
            j = i+1
            while j < len(nums) and nums[j] == v:
                nums[j] = None
                j += 1
        
        slow = 0
        while slow < len(nums) and nums[slow] is not None:
            slow += 1
        
        if slow == len(nums):
            return slow
        
        fast = slow+1
        while fast < len(nums):
            while nums[fast] is None:
                fast += 1
                if fast == len(nums):
                    return slow
            nums[slow], nums[fast] = nums[fast], None
            slow += 1
            fast += 1
        
        return slow
            