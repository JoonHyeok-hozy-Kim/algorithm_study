class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        M = {}
        result = 0
        for i, v in enumerate(nums1):
            for j, u in enumerate(nums2):
                if v+u not in M:
                    M[v+u] = 1
                else:
                    M[v+u] += 1
        
        for i, v in enumerate(nums3):
            for j, u in enumerate(nums4):
                if -(v+u) in M:
                    result += M[-(v+u)]
        
        return result