class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        
        result = 1
        if n > 0:
            if n // 2 > 0:
                result *= self.myPow(x*x, n//2)
            if n % 2 == 1:
                result *= x
                
        return result
            
            
            