"""
https://www.acmicpc.net/problem/1912
"""


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    dp = [0] * N
    dp[0] = nums[0]

    for i in range(1, N):
        if dp[i-1] < 0 or dp[i-1] + nums[i] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]


        # print(dp)

    print(max(dp))
