class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def counter_check(cntr):
            for k in cntr:
                if cntr[k] > 0:
                    return False
            return True
            
        curr_cntr = Counter(t)
        si = ei = 0
        sr = er = None
        checked = False

        while ei < len(s):
            if s[ei] in curr_cntr:
                curr_cntr[s[ei]] -= 1
            
            if not checked:
                if counter_check(curr_cntr):
                    checked = True
                
            if checked:
                while si < ei:
                    if s[si] in curr_cntr:
                        if curr_cntr[s[si]] < 0:
                            curr_cntr[s[si]] += 1
                            si += 1
                        else:
                            break
                    else:
                        si += 1

                if sr is None:
                    sr, er = si, ei
                elif er-sr > ei-si:
                    sr, er = si, ei
            
            ei += 1

        if sr is None:
            return ""
        else:
            return s[sr:er+1]