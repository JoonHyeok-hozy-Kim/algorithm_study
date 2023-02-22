# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.find_bad_version(0, n) + 1
        
    def find_bad_version(self, start, end):
        if start == end:
            return None
        
        mid = (start + end) // 2
        if (isBadVersion(mid+1)):
            result = mid
            temp = self.find_bad_version(start, mid)
            if temp is not None:
                result = temp
        else:
            result = None
            temp = self.find_bad_version(mid+1, end)
            if temp is not None:
                result = temp
        
        return result