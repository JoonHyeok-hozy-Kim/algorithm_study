class Solution:
    def rob(self, nums: List[int]) -> int:
        l1 = [nums[0]]
        l2 = [0]
        
        for i in range(1, len(nums)):
            l1.append(l2[i-1] + nums[i])
            l2.append(max(l1[i-1], l2[i-1]))
        
        return max(l1[-1], l2[-1])