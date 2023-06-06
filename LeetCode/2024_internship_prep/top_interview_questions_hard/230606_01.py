class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        H = []
        for x in nums1:
            heappush(H, x)
        for y in nums2:
            heappush(H, y)
        
        temp = [None, None]
        for i in range(N//2 + 1):
            temp[i%2] = heappop(H)
        
        if N % 2 == 0:
            return sum(temp) / 2
        else:
            return temp[(N//2) % 2]