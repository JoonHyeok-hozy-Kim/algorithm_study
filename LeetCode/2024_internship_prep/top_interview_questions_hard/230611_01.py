from math import inf

class Solution:
    def maxProfit(self, prices: list) -> int:
        sold = 0
        hold = -inf
        rest = 0

        for i in range(len(prices)):
            prev_sold = sold
            sold = hold + prices[i]
            hold = max(hold, rest-prices[i])
            rest = max(rest, prev_sold)

            print('\nsold : {}, hold : {}, rest : {}, prices[i] : {}'.format(sold, hold, rest, prices[i]))
        
        return max(sold, rest)

if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit([2,1,2,1,0,1,2,4,5,6,7]))