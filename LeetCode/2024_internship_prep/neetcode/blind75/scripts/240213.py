class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        MV = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        def _scan_land(i, j):
            if i < 0 or i == m or j < 0 or j == n:
                return
            
            if grid[i][j] != '1':
                return
            
            grid[i][j] = '2'
            for ii, jj in MV:
                _scan_land(i+ii, j+jj)
            
            return
        

        count = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == '1':
                    _scan_land(i, j)
                    count += 1
        
        return count