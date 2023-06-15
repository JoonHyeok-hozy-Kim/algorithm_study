from heapq import heappush, heappop

class Solution:
    def maxCoins(self, nums: list) -> int:
        dp = [[None for _ in range(300+2)] for _ in range(300+2)]
        new_nums = [1]
        new_nums.extend(nums)
        new_nums.append(1)

        def _recursive(i, j):
            if i > j:
                return 0
            
            if dp[i][j]:
                return dp[i][j]

            if i == j:
                result = new_nums[i]
                result *= new_nums[i-1]
                result *= new_nums[i+1]

            else:
                result = 0
                for k in range(i, j+1):
                    temp = new_nums[k]
                    temp *= new_nums[i-1]
                    temp *= new_nums[j+1]
                    temp += _recursive(i, k-1) + _recursive(k+1, j)
                    result = max(result, temp)

            dp[i][j] = result
            return result

        return _recursive(1, len(nums))



if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3,1,5,8]))

'''
1 : 2 * 1 * 5 = 10
2 : 3 * 2 * 5 = 30 -> 300

'''