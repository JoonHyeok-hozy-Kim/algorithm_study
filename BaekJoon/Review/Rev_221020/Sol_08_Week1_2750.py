"""
https://www.acmicpc.net/problem/2750
"""

if __name__ == '__main__':
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    # print(nums)

    for i in sorted(nums):
        print(i)