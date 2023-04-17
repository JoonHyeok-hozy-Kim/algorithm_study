class Solution:
    def calculate(self, s: str) -> int:
        S = []
        idx = 0
        temp_int, sign = 0, 1
        execute = None
        
        while True:
            if idx == len(s):
                if execute == '*':
                    S[-1] *= temp_int
                elif execute == '/':
                    if S[-1] * temp_int >= 0 or S[-1] % temp_int == 0:
                        S[-1] //= temp_int
                    else:
                        S[-1] //= temp_int
                        S[-1] += 1
                else:
                    S.append(temp_int * sign)
                break
            
            if s[idx] == ' ':
                None
            elif '0' <= s[idx] <= '9':
                temp_int *= 10
                temp_int += int(s[idx])
            else:
                S.append(temp_int * sign)
                temp_int, sign = 0, 1
                
                if execute:
                    popped = S.pop()
                    if execute == '*':
                        S[-1] *= popped
                    else:
                        if S[-1] * popped >= 0 or S[-1] % popped == 0:
                            S[-1] //= popped
                        else:
                            S[-1] //= popped
                            S[-1] += 1
                execute = None
                
                if s[idx] in ('*', '/'):
                    execute = s[idx]
                elif s[idx] == '-':
                    sign = -1
            
            idx += 1
        
        return sum(S)
                