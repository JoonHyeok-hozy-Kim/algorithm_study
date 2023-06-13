class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        M = defaultdict(list)
        for word in wordDict:
            M[word[0]].append(word)
        
        dp = [False] * len(s)
        Q = deque()
        Q.append(0)
        
        while Q:
            popped = Q.popleft()
            if popped == len(s):
                return True
            
            if dp[popped] or s[popped] not in M:
                continue
            
            dp[popped] = True
            for word in M[s[popped]]:
                if popped + len(word) - 1 >= len(s):
                    continue
                
                if s[popped : popped + len(word)] == word:
                    Q.append(popped + len(word))
        
        return False