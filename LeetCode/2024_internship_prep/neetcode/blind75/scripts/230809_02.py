class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        M = {}
        for ss in s:
            if ss in M:
                M[ss] += 1
            else:
                M[ss] = 1
        
        for tt in t:
            if tt in M:
                if M[tt] == 1:
                    del M[tt]
                else:
                    M[tt] -= 1
            else:
                return False
        
        if len(M) == 0:
            return True
        return False