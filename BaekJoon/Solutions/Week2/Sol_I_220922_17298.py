"""
17298. 오큰수
https://www.acmicpc.net/problem/17298
"""


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    S = []
    result = [None for _ in range(N)]
    for i in range(N):
        while len(S) > 0 and nums[S[-1]] < nums[i]:
            result[S.pop()] = str(nums[i])
        S.append(i)
    while len(S) > 0:
        result[S.pop()] = str(-1)

    print(' '.join(result))
