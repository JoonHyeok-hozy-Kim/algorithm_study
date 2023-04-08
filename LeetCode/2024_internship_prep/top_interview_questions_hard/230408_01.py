class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        curr live - next dead : 3
        curr dead - next live : 2
        '''
        m, n = len(board), len(board[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        alive = [1, 3]
        
        def _validate(x, y, neighbor):
            if 0 <= x + neighbor[0] < m and 0 <= y + neighbor[1] < n:
                return True
            return False
        
        def _next_status(x, y):
            live_cnt = 0
            for neighbor in neighbors:
                if _validate(x, y, neighbor):
                    if board[x+neighbor[0]][y+neighbor[1]] in alive:
                        live_cnt += 1
                        
            if board[x][y] in alive:
                if live_cnt < 2 or live_cnt > 3:
                    board[x][y] = 3
            else:
                if live_cnt == 3:
                    board[x][y] = 4
        
        for xx, row in enumerate(board):
            for yy, val in enumerate(row):
                _next_status(xx, yy)
        
        for xx, row in enumerate(board):
            for yy, val in enumerate(row):
                if val == 3:
                    board[xx][yy] = 0
                elif val == 4:
                    board[xx][yy] = 1
        