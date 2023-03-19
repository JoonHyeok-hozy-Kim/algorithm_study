class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self._recursive(nums, 0, len(nums)-1, result)
        return result
        
    def _recursive(self, nums, left, right, R):
        if left == right:
            R.append(nums[:])
            return
        
        for i in range(left, right+1):            
            nums[left], nums[i] = nums[i], nums[left]
            self._recursive(nums, left+1, right, R)
            nums[left], nums[i] = nums[i], nums[left]
            