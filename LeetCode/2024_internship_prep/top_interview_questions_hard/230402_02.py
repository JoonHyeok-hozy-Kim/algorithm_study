class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = 0
        left = -1
        down = len(matrix)
        right = len(matrix[0])
        result = [None] * (down * right)
        
        i = j = cnt = 0
        while up < down or left < right:
            while j < right-1 and left < right and cnt < len(result):
                result[cnt] = matrix[i][j]
                j += 1
                cnt += 1
            right -= 1
            
            while i < down-1 and up < down and cnt < len(result):
                result[cnt] = matrix[i][j]
                i += 1
                cnt += 1
            down -= 1
            
            while j > left+1 and left < right and cnt < len(result):
                result[cnt] = matrix[i][j]
                j -= 1
                cnt += 1
            left += 1
            
            while i > up+1 and up < down and cnt < len(result):
                result[cnt] = matrix[i][j]
                i -= 1
                cnt += 1
            up += 1
        
        if cnt < len(result):
            result[cnt] = matrix[i][j]
        return result
            