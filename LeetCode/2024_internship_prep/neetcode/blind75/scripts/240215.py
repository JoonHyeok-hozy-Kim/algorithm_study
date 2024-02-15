class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        MV = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]

        def _dfs(i, j, B, prev=0):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if B[i][j] == 1 or heights[i][j] < prev:
                return

            B[i][j] = 1
            for ii, jj in MV:
                _dfs(i+ii, j+jj, B, heights[i][j])


        for j in range(n):
            _dfs(0, j, pacific)
        for i in range(m):
            _dfs(i, 0, pacific)

        for j in range(n):
            _dfs(m-1, j, atlantic)
        for i in range(m):
            _dfs(i, n-1, atlantic)
        
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        return result