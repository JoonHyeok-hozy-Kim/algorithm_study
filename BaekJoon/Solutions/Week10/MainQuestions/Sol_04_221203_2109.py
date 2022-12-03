"""
https://www.acmicpc.net/problem/2109
"""
from heapq import heappop, heappush, heapify


if __name__ == "__main__":
    N = int(input())
    in_day_order = [None]
    for i in range(N):
        p, d = map(int, input().split())
        if d > len(in_day_order)-1:
            for j in range(d-len(in_day_order)+1):
                in_day_order.append(None)
            max_day = d
        if in_day_order[d] is None:
            in_day_order[d] = []
        in_day_order[d].append(-p)

    # print(in_day_order)

    revenue = 0
    day = len(in_day_order) - 1
    available_lectures = []
    # print(available_lectures)
    while day > 0:
        if in_day_order[day] is not None:
            for p in in_day_order[day]:
                heappush(available_lectures, p)
        if len(available_lectures) > 0:
            payment = heappop(available_lectures)
            revenue -= payment
        # print('day : {}, revenue : {}'.format(day, revenue))
        day -= 1
    print(revenue)