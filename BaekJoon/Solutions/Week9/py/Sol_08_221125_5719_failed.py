"""
https://www.acmicpc.net/problem/5719
"""
from heapq import heappop, heappush
from copy import deepcopy


def get_shortest_paths(n, s, d, R, road_trim=True):
    visited = [None] * n
    visited[s] = [0, dict()]
    heap = []
    heappush(heap, (0, s))
    final_min_length = None
    while heap:
        popped_length, popped = heappop(heap)
        # print('\nvisited : {}'.format(visited))
        # print('popped_length : {}, popped : {}'.format(popped_length, popped))

        if popped == d:
            if final_min_length is None or final_min_length > popped_length:
                final_min_length = popped_length

        if final_min_length is not None and final_min_length < popped_length:
            continue

        if R[popped] is not None:
            for linked in R[popped]:
                new_length = popped_length + R[popped][linked]
                if final_min_length is not None and final_min_length < new_length:
                    continue

                del_candidate = (popped, linked)    # Candidate for the part of the shortest path

                if visited[linked] is None or visited[linked][0] > new_length:
                    visited[linked] = [new_length, dict()]
                    visited[linked][1][del_candidate] = True

                elif visited[linked][0] == new_length:
                    visited[linked][1][del_candidate] = True

                else:
                    continue

                for prev_del in visited[popped][1]:
                    visited[linked][1][prev_del] = True
                heappush(heap, (new_length, linked))

    if final_min_length is not None and road_trim:
        if visited[d] is not None:
            for path in visited[d][1]:
                if path[1] in R[path[0]]:
                    del R[path[0]][path[1]]

    return final_min_length



if __name__ == '__main__':

    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break

        S, D = map(int, input().split())
        roads = [None] * N
        for _ in range(M):
            u, v, p = map(int, input().split())
            if roads[u] is None:
                roads[u] = {}
            roads[u][v] = p

        min_len = get_shortest_paths(N, S, D, roads, True)
        # print(path_list)
        # print('roads before : {}'.format(roads))

        if min_len is None:
            print(-1)

        else:
            final_len = get_shortest_paths(N, S, D, roads, False)
            print(-1) if final_len is None else print(final_len)
