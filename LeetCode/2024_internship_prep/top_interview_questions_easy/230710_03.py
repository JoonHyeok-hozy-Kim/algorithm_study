# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                if left == mid:
                    return right
                left = mid
        
        return left

                
'''
1 2 3 4 5 6 7 8

  v

1 8 -> 4
1 4 -> 2
1 2 -> 1

'''