class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, large = inf, inf
        for n in nums:
            if n <= small:
                small = n
            elif n <= large:
                large = n
            else:
                return True
        return False
        
        
    def second_increasingTriplet(self, nums: List[int]) -> bool:
        c1 = nums[0]
        c2 = [nums[0]]
        
        for i in range(1, len(nums)):
            v = nums[i]
            
            if len(c2) == 2:
                if v > c2[1]:
                    return True
                elif c1 < v <= c2[1]:
                    c2 = [c1, v]
                else:
                    c1 = v
            
            else:
                if v > c1:
                    c2 = [c1, v]
                else:
                    c1 = v
                    c2 = [v]
        
        return False