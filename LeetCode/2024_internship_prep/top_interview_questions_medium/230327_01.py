class Solution:
    def trailingZeroes(self, n: int) -> int:
        power = 5
        cnt = 0
        
        while power <= n:
            cnt += n // power
            power *= 5
        
        return cnt