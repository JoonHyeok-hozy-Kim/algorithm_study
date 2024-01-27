class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        result = []
        MOVES = [(1,0), (0, 1), (-1, 0), (0, -1)]
        T = {}

        # Build a trie with words.
        for word in words:
            for i, c in enumerate(word):
                if i == 0:
                    curr = T
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['%'] = word
        # print(T)

        def _dfs(i, j, curr):
            if '%' in curr:
                result.append(curr['%'])
                del curr['%']

            if i < 0 or i == m or j < 0 or j == n:
                return 

            if board[i][j] not in curr or board[i][j] == '*':
                return 
            
            copy = board[i][j]
            # print(copy)
            board[i][j] = '*'
            for (ii, jj) in MOVES:
                trunc_target = _dfs(i+ii, j+jj, curr[copy])
                if len(curr[copy]) == 0:
                    del curr[copy]
                    break
            board[i][j] = copy           

            return

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                _dfs(i, j, T)
                
        return result        