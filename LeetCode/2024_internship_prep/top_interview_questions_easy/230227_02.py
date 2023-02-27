from math import ceil, sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        L = [True] * n
        
        root = ceil(sqrt(n))
        for i in range(2, root):
            if L[i]:
                for j in range(i*i, n, i):
                    L[j] = False
        
        cnt = 0
        for i in range(2, n):
            if L[i]:
                cnt += 1
        
        return cnt