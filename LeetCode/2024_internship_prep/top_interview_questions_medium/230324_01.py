class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        r, c = 0, col-1
        
        while r < row and col >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            elif val < target:
                r += 1
            else:
                c -= 1
                
        return False