class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_cnt = 0
        Q = deque()
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "1":
                    Q.append((i, j))
        
        while Q:
            x, y = Q.popleft()
            if grid[x][y] == "1":
                island_cnt += 1
                self._dfs(grid, x, y)
        
        return island_cnt
    
    
    def _dfs(self, grid, x, y):
        grid[x][y] = "-1"
        if self._validate(grid, x-1, y):
            self._dfs(grid, x-1, y)
        if self._validate(grid, x+1, y):
            self._dfs(grid, x+1, y)
        if self._validate(grid, x, y-1):
            self._dfs(grid, x, y-1)
        if self._validate(grid, x, y+1):
            self._dfs(grid, x, y+1)
    
    
    def _validate(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] in ("0", "-1"):
            return False
        return True