class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        M = {}
        for word in strs:            
            temp_sorted = str(sorted(word))
            if temp_sorted not in M:
                M[temp_sorted] = []
            M[temp_sorted].append(word)
        
        result = []
        for k in M:
            temp = []
            for j in M[k]:
                temp.append(j)
            result.append(temp)
        
        return result