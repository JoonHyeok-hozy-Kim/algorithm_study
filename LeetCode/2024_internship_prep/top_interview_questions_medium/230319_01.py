class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self._recursive(nums, 0, len(nums), result)
        return result
        
        
    def _recursive(self, nums, start, end, R):
        if start == end:
            R.append(nums[:])
            return
        
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            self._recursive(nums, start+1, end, R)
            nums[start], nums[i] = nums[i], nums[start]
            