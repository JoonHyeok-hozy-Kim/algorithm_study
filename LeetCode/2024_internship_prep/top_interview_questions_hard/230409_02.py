class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = tortoise = 0
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            
            if hare == tortoise:
                break
        
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare