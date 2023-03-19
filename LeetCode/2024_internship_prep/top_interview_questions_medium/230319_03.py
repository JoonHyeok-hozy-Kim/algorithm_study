class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        xx, yy = [1, -1, 0, 0], [0, 0, 1, -1]
        ROWS, COLS = len(board), len(board[0])
        
        board_char_cnt = Counter(sum(board, []))
        for c, c_cnt in Counter(word).items():
            if board_char_cnt[c] < c_cnt:
                return False
        
        if word.count(word[0]) < word.count(word[-1]):
            word = word[::-1]
        
        def _dfs(i, j, cnt):
            if i < 0 or i >= ROWS:
                return False
            if j < 0 or j >= COLS:
                return False
            if board[i][j] is None:
                return False
            if cnt == len(word):
                return False
            if word[cnt] != board[i][j]:
                return False
            if cnt + 1 == len(word):
                return True
        
            curr_char, board[i][j] = board[i][j], None
            
            for k in range(4):
                if _dfs(i+xx[k], j+yy[k], cnt+1):
                    return True
            
            board[i][j] = curr_char
            return False
        
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if _dfs(i, j, 0):
                    return True
                
        return False