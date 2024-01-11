class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        diff = ord('a') - ord('A')

        while 0 <= left < right < len(s):
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left] != s[right]:
                    if s[left].isalpha() and s[right].isalpha():
                        if ord(s[left]) + diff != ord(s[right]):
                            if ord(s[left]) - diff != ord(s[right]):
                                return False
                    else:
                        return False
                left += 1
                right -= 1
        
        return True