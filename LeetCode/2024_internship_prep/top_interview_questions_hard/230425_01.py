class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        if endWord not in wordList:
            return 0
        
        patterns = defaultdict(set)
        visited = set()
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                patterns[p].add(word)
        
        Q = deque()
        Q.append((1, beginWord))
        visited.add(beginWord)
        
        while Q:
            cnt, curr = Q.popleft()
            
            if curr == endWord:
                return cnt
            
            for i in range(len(curr)):
                p = curr[:i] + "*" + curr[i+1:]
                for word in patterns[p]:
                    if word not in visited:
                        Q.append((cnt+1, word))
                        visited.add(word)
        
        return 0
                    