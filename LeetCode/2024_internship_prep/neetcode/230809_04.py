class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M = {}
        for i, n in enumerate(nums):
            if n in M:
                return [i, M[n]]
            else:
                M[target-n] = i