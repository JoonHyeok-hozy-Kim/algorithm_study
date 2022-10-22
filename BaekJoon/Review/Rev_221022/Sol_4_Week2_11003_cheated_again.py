"""
https://www.acmicpc.net/problem/11003
"""

from collections import deque
from heapq import heappush, heappop


if __name__ == '__main__':
    N, L = map(int, input().split())
    nums = list(map(int, input().split()))

    Q = deque()
    for i in range(N):
        if i-L+1 > 0:
            if Q[0] == nums[i-L]:
                Q.popleft()

        while len(Q) > 0 and Q[-1] > nums[i]:
            Q.pop()
        Q.append(nums[i])
        # print(Q)
        print(Q[0], end=" ")