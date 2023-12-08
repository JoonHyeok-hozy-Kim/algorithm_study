class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        max_len = largest_cnt = 0

        for i in range(len(s)):
            window[s[i]] += 1
            largest_cnt = max(largest_cnt, window[s[i]])

            if max_len - largest_cnt >= k:
                window[s[i-max_len]] -= 1
            else:
                max_len += 1
        
        return max_len