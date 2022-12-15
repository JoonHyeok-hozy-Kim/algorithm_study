"""
2493. 탑
https://www.acmicpc.net/problem/2493
"""
from collections import deque


if __name__ == '__main__':
    N = int(input())
    towers = list(map(int, input().split()))
    blockers = deque()

    for i in range(0, N):
        if len(blockers) == 0:
            print(0, end=" ")
        elif towers[blockers[len(blockers)-1]] <= towers[i]:
            blockers.clear()
            print(0, end=" ")
        else:
            while towers[blockers[0]] < towers[i]:
                blockers.popleft()
            print(blockers[0]+1, end=" ")

        blockers.appendleft(i)
        # print(blockers)
