class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        accum = 0
        result = -inf
        
        for i, v in enumerate(nums):
            curr = accum + v
            result = max(result, curr)
            
            accum = curr if curr > 0 else 0
        
        return result
    
'''
-3 1 3 5 -7 1 2 9 

accum  : 14
curr   : 14
result : 14

'''