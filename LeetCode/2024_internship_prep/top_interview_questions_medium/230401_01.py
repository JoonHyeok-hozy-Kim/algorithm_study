class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []
        for i, v in enumerate(tokens):
            if v == '+':
                a, b = S.pop(), S.pop()
                S.append(a + b)
            elif v == '-':
                a, b = S.pop(), S.pop()
                S.append(b - a)
            elif v == '*':
                a, b = S.pop(), S.pop()
                S.append(a * b)
            elif v == '/':
                a, b = S.pop(), S.pop()
                S.append(int(b/a))                
            else:
                S.append(int(v))
        return S.pop()