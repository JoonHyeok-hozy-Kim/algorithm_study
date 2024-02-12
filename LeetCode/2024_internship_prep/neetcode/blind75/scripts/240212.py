class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        MV = ((1, 0), (-1, 0), (0, 1), (0, -1))
        T = {}

        t = T
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['%'] = True

        def _dfs(i, j, curr, depth=0):
            if '%' in curr:
                # print('Found!')
                del curr['%']
                return True
            
            if i < 0 or i == m or j < 0 or j == n:
                return False
            
            if board[i][j] == '*' or board[i][j] not in curr:
                return False
            
            cc, board[i][j] = board[i][j], '*'
            after = curr[cc]

            # for _ in range(depth):
            #     print(' ', end="")
            # print('{}-{}'.format(cc, (i,j)))

            for ii, jj in MV:
                if _dfs(i+ii, j+jj, after, depth+1):
                    if len(after) == 0:
                        del curr[cc]
                    return True
            board[i][j] = cc

            return False
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if _dfs(i, j, T):
                    return True
        
        return False