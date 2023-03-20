class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        dp = [None] * ((10**4) * 2 + 1)
        max_idx = 0
        
        for i, v in enumerate(nums):
            max_idx = max(max_idx, v + (10**4))
            dp[v + (10**4)] = True
        
        print(len(dp), max_idx)
            
        while k > 1:
            max_idx -= 1
            while dp[max_idx] is None:
                max_idx -= 1
            k -= 1
            print(k, max_idx)
        
        return max_idx - 10**4

if __name__ == '__main__':
    s = Solution()
    a = [i for i in range(10)]
    print(s.findKthLargest(a, 3))