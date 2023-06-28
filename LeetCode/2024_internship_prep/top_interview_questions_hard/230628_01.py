class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        S = [(0, inf)]
        result = []
        curr_height = 0
        curr_end = inf
        idx = 0
        
        for b in buildings:            
            while curr_end < b[0]:
                while S[0][1] <= curr_end:
                    heappop(S)
                if curr_height > -S[0][0]:
                    result.append([curr_end, -S[0][0]])
                curr_height, curr_end = -S[0][0], S[0][1]
            
            heappush(S, (-b[2], b[1]))
            if b[2] <= curr_height:
                continue
            
            curr_height = b[2]
            curr_end = b[1]
            
            if len(result) > 0 and result[-1][0] == b[0]:
                if result[-1][1] < b[2]:
                    result[-1][1] = b[2]
            else:
                result.append([b[0], b[2]])
        
        while True:
            while S[0][1] <= curr_end:
                heappop(S)
            if curr_height > -S[0][0]:
                result.append([curr_end, -S[0][0]])
            
            if len(S) == 1:
                break
                
            curr_height, curr_end = -S[0][0], S[0][1]
        
        return result
            