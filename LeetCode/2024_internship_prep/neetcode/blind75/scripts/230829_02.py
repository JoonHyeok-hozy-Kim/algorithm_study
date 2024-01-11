class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        prev_min = prices[0]

        for i, p in enumerate(prices):
            prev_min = min(prev_min, p)
            result = max(result, p-prev_min)
        
        return result