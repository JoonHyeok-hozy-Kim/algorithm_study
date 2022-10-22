"""
https://www.acmicpc.net/problem/10975
"""

from collections import deque


if __name__ == '__main__':
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    s_nums = sorted(nums)
    # print(nums)
    # print(s_nums)

    indices = []
    D = []
    for n in nums:
        indices.append(s_nums.index(n))
    # print(indices)

    for i in indices:
        not_appended = True
        for d in D:
            if d[0]-1 == i or d[-1]+1 == i:
                d.appendleft(i) if d[0]-1 == i else d.append(i)
                not_appended = False
                break

        if not_appended:
            temp = deque()
            temp.append(i)
            D.append(temp)

        # print(D)

    print(len(D))