class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        M = {}
        for word in strs:
            L = list(word)
            L.sort()
            T = tuple(L)
            if T in M:
                M[T].append(word)
            else:
                M[T] = [word]
        
        return [M[k] for k in M.keys()]