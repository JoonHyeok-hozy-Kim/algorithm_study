class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        class Trie:
            def __init__(self, _words):
                self._data = {}
                for _word in _words:
                    self.insert(_word)
            
            def insert(self, _word):
                t = self._data
                for c in _word:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                t['#'] = '#'
            
            def is_empty(self):
                return len(self._data) == 0
            
            def top(self):
                return self._data
                                 
        
        T = Trie(words)
        result = []       
        
        def _adjacents(i, j):
            for (x, y) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]) and board[i+x][j+y] != '*':
                    yield (i+x, j+y)
        
        def _dfs(i, j, t, temp=None, depth=0):
            # print('In _dfs({}, {})'.format(i, j), end="")
            # print(' '*depth)
            if temp is None:
                temp = []
            
            curr = board[i][j]
            if curr in t:
                next_t = t[curr]
                
                if '#' in next_t:
                    temp.append(curr)
                    result.append(''.join(temp))
                    temp.pop()
                    del next_t['#']
                
                if len(next_t):
                    board[i][j] = '*'
                    temp.append(curr)
                    for ai, aj in _adjacents(i, j):
                        _dfs(ai, aj, next_t, temp, depth+1)                
                    board[i][j] = curr
                    temp.pop()
                else:
                    del t[curr]
        
        # print('Trie Top : {}'.format(T.top()))/

        for i, row in enumerate(board):
            if T.is_empty():
                break
            for j, val in enumerate(row):
                if T.is_empty():
                    break
                _dfs(i, j, T.top())
        
        return result
                
        
if __name__ == '__main__':
    b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    w = ["oath","pea","eat","rain"]
    s = Solution()
    print(s.findWords(b, w))