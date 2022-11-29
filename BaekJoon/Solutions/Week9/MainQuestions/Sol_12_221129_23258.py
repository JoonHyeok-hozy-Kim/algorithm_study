"""
https://www.acmicpc.net/problem/23258
"""
from heapq import heappop, heappush
input = __import__('sys').stdin.readline


def find_shortest_path(N, D, C, s, e):
    total_capacity = 1 << C
    visited = [None] * (N+1)
    visited[s] = 0
    heap = []
    heappush(heap, (0, 0, s))
    min_final_distance = None
    while heap:
        popped_distance, prev_capacity, popped = heappop(heap)

        if popped == e:
            if prev_capacity < total_capacity and (min_final_distance is None or min_final_distance > popped_distance):
                min_final_distance = popped_distance
            else:
                continue

        if min_final_distance is not None and min_final_distance < popped_distance:
            continue

        curr_capacity = prev_capacity + (1 << popped) if popped != s else prev_capacity
        if curr_capacity >= total_capacity:
            continue

        for linked in range(1, N+1):
            if D[popped][linked] > 0:
                new_distance = popped_distance + D[popped][linked]
                if min_final_distance is not None and min_final_distance < new_distance:
                    continue

                if visited[linked] is None or visited[linked] > new_distance:
                    visited[linked] = new_distance
                    heappush(heap, (new_distance, curr_capacity, linked))

    return min_final_distance if min_final_distance is not None else -1


if __name__ == '__main__':
    N, Q = map(int, input().split())
    distances = [None] * (N+1)
    for i in range(1, N+1):
        temp = [None]
        for j in map(int, input().split()):
            temp.append(j)
        distances[i] = temp
    # print(distances)

    for _ in range(Q):
        C, s, e = map(int, input().split())
        result = find_shortest_path(N, distances, C, s, e)
        print(result)