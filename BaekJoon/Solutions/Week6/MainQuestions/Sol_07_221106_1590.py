"""
https://www.acmicpc.net/problem/1590
"""
from bisect import bisect_left


if __name__ == '__main__':
    N, T = map(int, input().split())
    schedule = []
    for _ in range(N):
        start, term, times = map(int, input().split())
        temp = [None] * times
        for i in range(times):
            temp[i] = start + term * i
        schedule.extend(temp)

    schedule.sort()
    # print(schedule)

    if T > schedule[-1]:
        print(-1)
    else:
        candidates = []
        target = bisect_left(schedule, T)
        temp = schedule[target] - T
        if temp >= 0:
            candidates.append(temp)
        if target + 1 < len(schedule):
            candidates.append(schedule[target+1] - T)
        print(min(candidates))