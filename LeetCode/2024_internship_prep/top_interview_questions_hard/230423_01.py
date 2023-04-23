class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue
            
            for word in wordDict:
                last_idx = i + len(word) - 1
                if last_idx + 1 < len(dp) and s[i:last_idx+1] == word:
                    dp[last_idx + 1] = True
                    if last_idx + 1 == len(s):
                        return True
        
        return dp[-1]

        ## s="aaaaaaaaaaaa", wordDict=["a","aa","aaa","aaaa"] 이 경우 시간초과
        # M = {}
        # def _dfs(idx):
        #     if idx not in M:
        #         return False
            
        #     for val in M[idx]:
        #         if val == len(s):
        #             return True
        #         elif _dfs(val):
        #             return True
            
        #     return False


        # for word in wordDict:
        #     for i in range(len(s)-len(word)+1): # abcd abc
        #         if word == s[i:i+len(word)]:
        #             if i not in M:
        #                 M[i] = []
        #             M[i].append(i+len(word))
        
        # if 0 in M:
        #     if _dfs(0):
        #         return True
        
        # return False