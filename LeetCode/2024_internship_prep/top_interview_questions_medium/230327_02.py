class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = len(columnTitle)
        P = 26**d
        idx = (P-26) // 25 + 1                  # 26(26**(d-1)-1)//25 + 1
        
        for i, v in enumerate(columnTitle):
            P //= 26
            diff = ord(v) - ord('A')
            idx += diff * P                     # 26**(d-i-1)
        
        return idx