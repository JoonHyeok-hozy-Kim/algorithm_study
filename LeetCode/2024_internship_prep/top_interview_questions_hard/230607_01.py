class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr, pos, neg = None, None, None
        result = nums[0]
        
        for i, v in enumerate(nums):
            result = max(result, v)
            
            if curr is None:
                if v == 0:
                    continue
                else:
                    curr = v
                    if v > 0:
                        pos = v
                    else:
                        neg = v
            
            else:
                if v == 0:
                    if pos:
                        result = max(result, pos)
                    curr = pos = neg = None
                elif v > 0:
                    if pos:
                        pos *= v
                    else:
                        pos = v
                    
                    if neg:
                        neg *= v
                        
                else:                    
                    if pos and neg:
                        result = max(result, pos)
                        pos, neg = neg * v, pos * v
                    elif pos:
                        result = max(result, pos)
                        neg = pos * v
                        pos = None
                    elif neg:
                        pos = neg * v
                        neg = v
                    else:
                        neg = v
        
        if curr and pos:
            result = max(result, pos)
        
        return result