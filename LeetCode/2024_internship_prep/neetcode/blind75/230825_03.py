class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dp = [None] * 2001
        # -1000 : 0
        # 0 : 1000
        # 1000 : 2000

        for i, n in enumerate(numbers):
            k = target - n + 1000
            if 0 <= k <= 2000:
                dp[k] = i+1
        
        for j, n in enumerate(numbers):
            if dp[n+1000]:
                temp = [j+1, dp[n+1000]]
                temp.sort()
                return temp