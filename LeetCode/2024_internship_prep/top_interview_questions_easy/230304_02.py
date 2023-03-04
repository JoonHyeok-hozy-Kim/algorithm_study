class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor > 0:
            if xor & 1:
                distance += 1
            xor >>= 1
        return distance