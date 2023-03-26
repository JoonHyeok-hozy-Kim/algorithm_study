class Solution:
    def isHappy(self, n: int) -> bool:
        def _calculate(n):
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n //= 10
            return result
        
        record = set()
        while True:
            if n == 1:
                return True
            n = _calculate(n)
            if n in record:
                return False
            record.add(n)