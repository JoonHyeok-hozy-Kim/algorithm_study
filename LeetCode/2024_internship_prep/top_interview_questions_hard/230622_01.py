class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1. DP : Create a list with the length of 10 and each element will be a list
        dp = [[] for _ in range(10)]
        result_list = []
        
        # 2. Categorize numbers into each ealement lists.
        for n in nums:
            sn = str(n)
            idx = int(sn[0])
            dp[idx].append(sn)
        
        # 3. Sort element-lists with the following Rule.
        
        # 3-1. Compare each digit of numbers starting from the most significant digit and choose the one with bigger number
        
        # 3-2. If there is a case that two numbers have different length and all the digits of the shorter one are identical to the starting digits of the longer one, "compare the first digit after identicals of the longer one with the most siginificant digit of the two. If the former is greater than the latter, choose longer one instead of the shorter one"
        def _greater(s1: str, s2: str) -> bool:
            if len(s1) >= len(s2):
                longer, shorter = s1, s2
                s1_long = True
            else:
                longer, shorter = s2, s1
                s1_long = False
                
            li = si = 0
            temp = None
            while si < len(shorter):
                if longer[li] > shorter[si]:
                    temp = True
                    break
                elif longer[li] < shorter[si]:
                    temp = False
                    break
                li += 1
                si += 1
            
            if temp is None:
                if len(longer) == len(shorter):
                    return True
                temp = _greater(longer[li:], shorter)
            
            if s1_long:
                return temp
            else:
                return not temp
        
        def _merge(L1, L2, L):
            i1, i2 = 0, 0
            while i1 + i2 < len(L):
                if i1 == len(L1) or (i2 < len(L2) and _greater(L2[i2], L1[i1])):
                    L[i1+i2] = L2[i2]
                    i2 += 1
                else:
                    L[i1+i2] = L1[i1]
                    i1 += 1
        
        def _sort(L: list) -> None:
            n = len(L)
            if n <= 1:
                return
            
            mid = n // 2
            L1 = L[:mid]
            L2 = L[mid:]
            _sort(L1)
            _sort(L2)
            _merge(L1, L2, L)        
        
        # 4. Choose numbers starting from the end of DP.
        for l in dp:
            _sort(l)
        
        for i, l in enumerate(dp[::-1]):
            for s in l:
                result_list.append(s)
        
        if result_list[0] == '0':
            return '0'
        return ''.join(result_list)