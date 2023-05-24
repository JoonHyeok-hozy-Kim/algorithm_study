class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def _is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def _sub_partition(i, j):            
            result = []
            k = i
            while k+1 <= j:
                if _is_palindrome(i, k):
                    x1 = s[i:k+1]
                    p2 = _sub_partition(k+1, j)
                    for x2 in p2:
                        temp = [x1]
                        temp.extend(x2)
                        result.append(temp)
                k += 1
            
            if _is_palindrome(i, k):
                result.append([s[i:k+1]])
            
            return result
        
        return _sub_partition(0, len(s)-1)