"""
11003. 최솟값 찾기
https://www.acmicpc.net/problem/11003
"""
from collections import deque

if __name__ == '__main__':
    N, L = map(int, input().split())
    nums = list(map(int, input().split()))

    candidates = deque()
    for i in range(N):
        min_idx = max(0, i - L + 1)
        while len(candidates) > 0 and candidates[0] < min_idx:
            candidates.popleft()

        while len(candidates) > 0 and nums[candidates[-1]] >= nums[i]:
            candidates.pop()

        candidates.append(i)

        print(nums[candidates[0]], end=" ")