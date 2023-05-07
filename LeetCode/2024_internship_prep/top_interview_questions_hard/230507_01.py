class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, j):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return
            if board[i][j] != 'O':
                return
            
            board[i][j] = 1
            for d in D:
                dfs(i+d[0], j+d[1])
        
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 1:
                    board[i][j] = 'O'
                elif val == 'O':
                    board[i][j] = 'X'