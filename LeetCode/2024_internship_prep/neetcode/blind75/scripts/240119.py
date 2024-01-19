class Trie:

    def __init__(self):
        self._data = {}

    def insert(self, word: str) -> None:
        curr = self._data
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['%'] = True

    def search(self, word: str) -> bool:
        curr = self._data
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        
        if '%' in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self._data
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        
        return True       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)