class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layer = n//2 if n%2 == 0 else n//2 + 1
        seq = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for i in range(layer):
            length = n - 2 * i
            points = [[i,i], [i, i+length-1], [i+length-1, i+length-1], [i+length-1, i]]
            
            for j in range(length-1):
                px, py = points[-1][0] + j*seq[-1][0], points[-1][1] + j*seq[-1][1]
                prev_val = matrix[px][py]
                
                for k in range(4):
                    x, y = points[k][0] + j*seq[k][0], points[k][1] + j*seq[k][1]                        
                    matrix[x][y], prev_val = prev_val, matrix[x][y]
                    # print(x, y)