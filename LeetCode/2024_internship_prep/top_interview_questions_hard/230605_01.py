class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)        
        if n == 1:
            return matrix[0][0]
        
        l, r = matrix[0][0], max(row[n-1] for row in matrix)
        
        while l < r:
            mid = (l+r)//2
            c = sum(bisect_right(row, mid) for row in matrix)
            if c < k:
                l = mid+1
            else:
                r = mid
        
        return l