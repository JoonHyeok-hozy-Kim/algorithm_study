class Trie:

    def __init__(self):
        self._dict = {}
        

    def insert(self, word: str) -> None:
        walk = self._dict
        idx = 0
        while idx < len(word):
            if word[idx] not in walk:
                walk[word[idx]] = {}
            walk = walk[word[idx]]
            idx += 1
        walk['*'] = None
        

    def search(self, word: str) -> bool:
        idx = 0
        walk = self._dict
        while True:
            if idx < len(word):
                if word[idx] in walk:
                    walk = walk[word[idx]]
                else:
                    return False
            else:
                if '*' in walk:
                    return True
                else:
                    return False
            idx += 1
        

    def startsWith(self, prefix: str) -> bool:
        idx = 0
        walk = self._dict
        while idx < len(prefix):
            if prefix[idx] in walk:
                walk = walk[prefix[idx]]
            else:
                return False
            idx += 1
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)