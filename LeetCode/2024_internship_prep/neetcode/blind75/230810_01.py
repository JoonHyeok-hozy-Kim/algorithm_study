class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)

        def _row_check(i):
            row = [None] * (N+1)
            for j in range(N):
                if board[i][j] == ".":
                    continue
                if row[int(board[i][j])]:
                    return False
                row[int(board[i][j])] = True
            return True
        
        def _col_check(j):
            col = [None] * (N+1)
            for i in range(N):
                if board[i][j] == ".":
                    continue
                if col[int(board[i][j])]:
                    return False
                col[int(board[i][j])] = True
            return True
        
        def _cube_check(i, j):
            col = [None] * (N+1)
            ii = i * 3
            jj = j * 3
            for iii in range(ii, ii+3):
                for jjj in range(jj, jj+3):
                    if board[iii][jjj] == ".":
                        continue
                    if col[int(board[iii][jjj])]:
                        return False
                    col[int(board[iii][jjj])] = True
            return True
                            

        for i in range(N):
            if not _row_check(i):
                return False
            
            if not _col_check(i):
                return False
            
        for i in range(3):
            for j in range(3):
                if not _cube_check(i, j):
                    return False
        
        return True