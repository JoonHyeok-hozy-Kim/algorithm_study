class Solution:
    def getSum(self, a: int, b: int) -> int:
        def pos_pos_sum(n1, n2):
            result = 0
            digit = 1
            while digit <= n1 or digit <= n2:
                d1 = n1 & digit
                d2 = n2 & digit
                
                if d1 & d2:
                    result |= digit << 1
                elif d1 != d2:
                    if result & digit:
                        result |= digit << 1
                        result = pos_neg_sum(result, -digit)
                    else:
                        result |= digit
                
                digit <<= 1
                
            return result
        
        def pos_neg_sum(n1, n2):
            # n1 > 0 and n2 < 0
            if n1 < -n2:
                return pos_neg_sum(-n2, -n1) * (-1)
            
            else:
                n2 = -n2
                result = 0
                digit = 1
                while digit <= n1:
                    digit <<= 1
                digit >>= 1
                
                while digit > 0:
                    result <<= 1
                    d1, d2 = n1 & digit, n2 & digit
                    
                    if d1 == digit and d2 != digit:
                        result |= 1
                    elif d1 != digit and d2 == digit:
                        temp = 1
                        while temp & result == 0:
                            temp <<= 1
                        tc = temp
                        while tc > 0:
                            result >>= 1
                            tc >>= 1
                        
                        result <<= 1
                        temp >>= 1
                        while temp > 0:
                            result |= 1
                            result <<= 1
                            temp >>= 1
                        result >>= 1
                        
                    digit >>= 1                
            
            return result
        
        
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a > 0 and b > 0:
            return pos_pos_sum(a, b)
        elif a < 0 and b < 0:
            return pos_pos_sum(-a, -b) * (-1)
        elif a > 0 and b < 0:
            return pos_neg_sum(a, b)
        else:
            return pos_neg_sum(b, a)