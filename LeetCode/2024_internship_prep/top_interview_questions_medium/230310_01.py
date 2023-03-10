class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        D = deque()
        S = set()
        max_len = 0
        
        for c in s:
            if c not in S:
                S.add(c)
            else:
                max_len = max(max_len, len(D))
                while D[0] != c:
                    S.remove(D.popleft())
                D.popleft()
            D.append(c)
                
        
        return max(max_len, len(D))