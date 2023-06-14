class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        M = defaultdict(list)
        for w in wordDict:
            M[w[0]].append(w)
        
        result = []
        sentence = []
        
        def _dfs(start, sl):
            if start == len(s):
                result.append(' '.join(sl))
                return
            
            a = s[start]
            if a not in M:
                return
            
            for w in M[a]:
                next_idx = start + len(w)
                if next_idx <= len(s):
                    if w == s[start : next_idx]:
                        sl.append(w)
                        _dfs(next_idx, sl)
                        sl.pop()
        
        _dfs(0, sentence)
        return result