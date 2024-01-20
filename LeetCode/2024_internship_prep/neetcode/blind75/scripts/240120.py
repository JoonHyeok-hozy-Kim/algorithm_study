class WordDictionary:

    def __init__(self):
        self._data = {}

    def addWord(self, word: str) -> None:
        curr = self._data
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['%'] = None

    def search(self, word: str) -> bool:
        def _recursive(curr, i):
            if curr is None:
                return False
            if i == len(word):                
                return True if '%' in curr else False

            if word[i] == '.':
                for k in curr:
                    found = _recursive(curr[k], i+1)
                    if found:
                        return True
            elif word[i] in curr:
                return _recursive(curr[word[i]], i+1)
            
            return False
        
        return _recursive(self._data, 0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)