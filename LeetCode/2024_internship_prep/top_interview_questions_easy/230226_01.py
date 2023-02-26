from copy import deepcopy
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = deepcopy(nums)

    def reset(self) -> List[int]:
        return self.original        

    def shuffle(self) -> List[int]:
        n = len(self.original)
        for i in range(n):
            rand = randint(0, n-1-i)
            self.nums.append(self.nums.pop(rand))
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()