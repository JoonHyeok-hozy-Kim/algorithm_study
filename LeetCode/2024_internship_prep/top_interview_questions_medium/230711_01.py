class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        
        M = defaultdict(int)
        for n in nums:
            M[n] += 1
                
        keys = list(M.keys())
        for i, ki in enumerate(keys):
            if ki == 0:
                if M[ki] >= 3:
                    result_set.add((0,0,0))
                
            else:
                if M[ki] >= 2 and ki*(-2) in M:
                    temp = [ki, ki, ki*(-2)]
                    temp.sort()
                    result_set.add(tuple(temp))
            
                for j, kj in enumerate(keys[i+1:]):
                    last = -(ki+kj)
                    if last in M and ki != last and kj != last:
                        temp = [ki, kj, -(ki+kj)]
                        temp.sort()
                        result_set.add(tuple(temp))
        
        return list(result_set)