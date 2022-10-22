"""
https://www.acmicpc.net/problem/17298
"""

from collections import deque


def original_solution(N, nums):
    result = deque()
    Q = deque()
    curr_max = None
    for i in range(N):
        not_inserted = True
        target = nums[N-1-i]
        if curr_max is None or target >= curr_max:
            Q.clear()
            curr_max = target
        else:
            while len(Q) > 0 and Q[0] <= target:
                Q.popleft()
            if len(Q) > 0:
                result.appendleft(Q[0])
                not_inserted = False
        Q.appendleft(target)
        if not_inserted:
            result.appendleft(-1)
        # print(result, Q)

    print(*result, sep=" ")


def alternative_solution(N, nums):
    S = []
    result = [None for _ in range(N)]

    for i in range(N):
        while len(S) > 0 and nums[S[-1]] < nums[i]:
            result[S.pop()] = str(nums[i])
        S.append(i)
        # print(result, S)

    while len(S) > 0:
        result[S.pop()] = str(-1)

    print(' '.join(result))



if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    # original_solution(N, nums)
    alternative_solution(N, nums)