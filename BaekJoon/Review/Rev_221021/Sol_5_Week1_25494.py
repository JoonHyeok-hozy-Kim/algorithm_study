"""
https://www.acmicpc.net/problem/25494

2
1 2 3
3 2 4

"""


def solution():
    nums = list(map(int, input().split()))
    result = 0
    for x in range(1, nums[0]+1):
        for y in range(1, nums[1]+1):
            for z in range(1, nums[2]+1):
                if x % y == y % z == z % x:
                    result += 1
    return result


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(solution())