class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for j in range(m)]
        
        def _dfs(i, j):
            if not dp[i][j]:
                curr = matrix[i][j]
                u = _dfs(i-1, j) if i-1 >= 0 and matrix[i-1][j] > curr else 0
                d = _dfs(i+1, j) if i+1 < m and matrix[i+1][j] > curr else 0
                l = _dfs(i, j-1) if j-1 >=0 and matrix[i][j-1] > curr  else 0
                r = _dfs(i, j+1) if j+1 < n and matrix[i][j+1] > curr else 0
                temp = max(u,d,l,r)+1
                dp[i][j] = max(dp[i][j], temp)
                
            return dp[i][j]
        
        return max(_dfs(x, y) for x in range(m) for y in range(n))