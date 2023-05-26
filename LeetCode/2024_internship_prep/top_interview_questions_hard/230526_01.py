class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:        
        temp = []
        set_result = set([""])
        result = []
        
        def _recursive(i, opened, closed):
            if i == len(s):
                if opened - closed == 0:
                    popped = set_result.pop()
                    if len(popped) < len(temp):
                        set_result.clear()
                        set_result.add(''.join(temp))
                    else:
                        set_result.add(popped)
                        if len(popped) == len(temp):
                            set_result.add(''.join(temp))
                return
                
            if s[i] == '(':
                temp.append('(')
                _recursive(i+1, opened+1, closed)                
                temp.pop()
                
                _recursive(i+1, opened, closed)
            
            elif s[i] == ')':
                if opened > closed:
                    temp.append(')')
                    _recursive(i+1, opened, closed+1)
                    temp.pop()
                _recursive(i+1, opened, closed)
            
            else:
                cnt = 0
                while i+cnt < len(s) and s[i+cnt] not in '()':
                    temp.append(s[i+cnt])
                    cnt += 1                    
                _recursive(i+cnt, opened, closed)
                for j in range(cnt):
                    temp.pop()
        
        _recursive(0, 0, 0)
        return list(set_result) if len(set_result) > 0 else [""]           
            