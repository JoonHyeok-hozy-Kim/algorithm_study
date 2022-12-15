"""
https://www.acmicpc.net/problem/1781
"""
from heapq import heappush, heappop, heapify


if __name__ == '__main__':
    N = int(input())
    in_day_order = [None]
    for _ in range(N):
        deadline, ramen = map(int, input().split())
        if len(in_day_order)-1 < deadline:
            for _ in range(deadline - len(in_day_order) + 1):
                in_day_order.append(None)
        if in_day_order[deadline] is None:
            in_day_order[deadline] = []
        in_day_order[deadline].append(-ramen)
        # print(in_day_order)

    day = len(in_day_order)-1
    availables = []
    total_ramens = 0
    while day > 0:
        if in_day_order[day] is not None:
            for r in in_day_order[day]:
                heappush(availables, r)
        if availables:
            total_ramens -= heappop(availables)
        day -= 1
    print(total_ramens)