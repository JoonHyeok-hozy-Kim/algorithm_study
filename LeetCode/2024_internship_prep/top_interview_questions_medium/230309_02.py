class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Q = deque()
        for i, ival in enumerate(matrix):
            for j, jval in enumerate(ival):
                if jval == 0:
                    Q.append((i, j))
        
        while len(Q) > 0:
            i, j = Q.popleft()
            up = i-1
            while up >= 0:
                matrix[up][j] = 0
                up -= 1
            down = i+1
            while down < len(matrix):
                matrix[down][j] = 0
                down += 1
            left = j-1
            while left >= 0:
                matrix[i][left] = 0
                left -= 1
            right = j+1
            while right < len(matrix[0]):
                matrix[i][right] = 0
                right += 1