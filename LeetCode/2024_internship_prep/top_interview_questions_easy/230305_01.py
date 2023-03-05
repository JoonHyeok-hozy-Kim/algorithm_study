class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        digit = 1
        for i in range(32):
            if digit & n:
                result += 1
            if i == 31:
                break
            result <<= 1
            digit <<= 1
        return result