class Solution:
    def __init__(self):
        return 
    
    def _solve(self, dp, i, j, s):
        if i == j:
            dp[i][j] = True
        elif j == i+1:
            if s[i] == s[j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        elif s[i] == s[j] and dp[i+1][j-1]:
            dp[i][j] = True
        else:
            dp[i][j] = False
    
    def print_dp(self, dp):
        for i in range(len(dp)):
            print("--", end="")
        print()

        for i in dp:
            for j in i:
                if j:
                    print("T ", end="")
                else:
                    print("F ", end="")
            print()
            
        for i in range(len(dp)):
            print("--", end="")
        print()

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        start = max_len = 0
        for g in range(n):
            i, j = 0, g
            while j < n:
                self._solve(dp, i, j, s)
                self.print_dp(dp)
                if dp[i][j] and j-i+1 > max_len:
                    start = i
                    max_len = j-i+1
                i += 1
                j += 1

        return s[start:start+max_len]

    # def longestPalindrome(self, s: str) -> str:
    #     result = deque()
    #     for i in range(len(s)):
    #         temp = deque()
    #         temp.append(s[i])
    #         left, right = i-1, i+1
    #         while left >=0 and right < len(s):
    #             if s[left] == s[right]:
    #                 temp.appendleft(s[left])
    #                 temp.append(s[right])
    #                 left -= 1
    #                 right += 1
    #             else:
    #                 break
    #         if len(temp) > len(result):
    #             result = temp
        
    #         if i > 0 and s[i-1] == s[i]:
    #             temp = deque()
    #             left, right = i-1, i
    #             while left >= 0 and right < len(s):
    #                 if s[left] == s[right]:
    #                     temp.appendleft(s[left])
    #                     temp.append(s[right])
    #                     left -= 1
    #                     right += 1
    #                 else:
    #                     break
    #             if len(temp) > len(result):
    #                 result = temp
                                    
    #     return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print("1. ", s.longestPalindrome('abcde'))
    print("2. ", s.longestPalindrome('abcede'))