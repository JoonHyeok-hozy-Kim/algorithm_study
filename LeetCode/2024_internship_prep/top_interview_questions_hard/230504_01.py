class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        M = {}
        max_len, most_used = 0, 0
        result = 0

        for i in range(len(s)):
            if s[i] not in M:
                M[s[i]] = 0
            M[s[i]] += 1

            most_used = max(most_used, M[s[i]])
            if max_len - most_used >= k:
                M[s[i-max_len]] -= 1
            else:
                max_len += 1
            result = max(result, max_len)
        
        return result