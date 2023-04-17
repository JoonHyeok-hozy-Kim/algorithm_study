from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_cnt = {}
        window = deque()
        t_set = set(t)
        start, end = None, None
        
        for c in t:
            if c in char_cnt:
                char_cnt[c] += 1
            else:
                char_cnt[c] = 1
        
        for i, c in enumerate(s):
            if c in char_cnt:
                while len(window) > 0 and \
                (char_cnt[window[0][0]] < 0 or (window[0][0] == c and char_cnt[c] == 0)):
                    popped = window.popleft()
                    char_cnt[popped[0]] += 1
                
                window.append((c, i))
                char_cnt[c] -= 1
                
                if char_cnt[c] == 0 and c in t_set:
                    t_set.remove(c)
                
                if len(t_set) == 0:
                    if start is None or end - start > window[-1][1] - window[0][1]:
                        start, end = window[0][1], window[-1][1]
                        popped = window.popleft()
                        char_cnt[popped[0]] += 1
                        t_set.add(popped[0])
        
        if start is None:
            return ""
        else:
            return s[start:end+1]