class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[m+n-1-i] = nums1[m-1-i]
        
        i1, i2 = 0, 0
        while i1+i2 < m+n:
            if i2 == n or (i1 < m and nums1[i1+n] < nums2[i2]):
                nums1[i1+i2] = nums1[i1+n]
                i1 += 1
            else:
                nums1[i1+i2] = nums2[i2]
                i2 += 1
        