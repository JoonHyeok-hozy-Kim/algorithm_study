"""
https://www.acmicpc.net/problem/11779
"""
from heapq import heappop, heappush
from copy import deepcopy


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    buses = [None] * (N+1)
    for _ in range(M):
        s, e, cost = map(int, input().split())
        if buses[s] is None:
            buses[s] = dict()
        buses[s][e] = cost if e not in buses[s] else min(buses[s][e], cost)
    sp, ep = map(int, input().split())

    cost_records = [None] * (N+1)
    cost_records[sp] = 0
    heap = []
    heappush(heap, (0, sp, [sp]))
    min_final_cost = None
    min_final_route = None
    while heap:
        popped_cost, popped, popped_route = heappop(heap)
        if popped == ep:
            if min_final_cost is None or popped_cost < min_final_cost:
                min_final_cost = popped_cost
                min_final_route = popped_route

        if min_final_cost is None or min_final_cost >= popped_cost:
            if buses[popped] is not None:
                for linked in buses[popped]:
                    additional_cost = buses[popped][linked]
                    if min_final_cost is None or min_final_cost >= popped_cost + additional_cost:
                        if cost_records[linked] is None or cost_records[linked] > popped_cost + additional_cost:
                            new_route = deepcopy(popped_route)
                            new_route.append(linked)
                            cost_records[linked] = popped_cost + additional_cost
                            heappush(heap, (popped_cost + additional_cost, linked, new_route))

    print(min_final_cost)
    print(len(min_final_route))
    print(*min_final_route, sep=" ")