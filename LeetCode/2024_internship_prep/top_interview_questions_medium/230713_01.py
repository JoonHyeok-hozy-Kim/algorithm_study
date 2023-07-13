class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        S = [[]]
        
        for n in nums:
            SS = []
            
            for s in S:
                N = len(s)+1
                for i in range(N):
                    temp = [None] * N
                    j = cnt = 0
                    while j < N:
                        if i == j:
                            temp[j] = n
                        else:
                            temp[j] = s[cnt]
                            cnt += 1
                        j += 1        
                        
                    SS.append(temp)
            
            S = SS
        
        return S