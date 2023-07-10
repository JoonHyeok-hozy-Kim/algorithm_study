class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        
        N = 1<<31
        
        if x == 0:
            return 0
        
        else:
            neg = 1 if x > 0 else -1                
            x *= neg                
            
            while x > 0:
                result *= 10
                result += x % 10
                x //= 10

        if (neg < 0 and -result < -N) or (neg > 0 and result > N-1):
            return 0
        
        return result * neg