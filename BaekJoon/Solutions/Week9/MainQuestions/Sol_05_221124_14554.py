"""
https://www.acmicpc.net/problem/14554
"""
from heapq import heappush, heappop
input = __import__('sys').stdin.readline


if __name__ == '__main__':
    N, M, S, E = map(int, input().split())

    edges = [None] * (N+1)
    for _ in range(M):
        a, b, c = map(int, input().split())
        if edges[a] is None:
            edges[a] = {}
        if b not in edges[a] or c < edges[a][b][0]:
            edges[a][b] = [c, 1]
        elif c == edges[a][b][0]:
            edges[a][b][1] += 1

        if edges[b] is None:
            edges[b] = {}
        edges[b][a] = edges[a][b]
    # print(edges)

    visited = [None] * (N+1)
    visited[S] = 0
    heap = []
    heappush(heap, (0, 1, S))   # distance, cnt, starting_point
    min_distance_to_E = None
    min_distance_cnt = 0
    while heap:
        popped_distance, popped_cnt, popped = heappop(heap)
        if popped == E:
            if min_distance_to_E is None or min_distance_to_E > popped_distance:
                min_distance_to_E = popped_distance
                min_distance_cnt = popped_cnt
            elif min_distance_to_E == popped_distance:
                min_distance_cnt += popped_cnt

            if min_distance_cnt >= (10**9 + 9):
                min_distance_cnt %= 10**9 + 9

        if edges[popped] is not None:
            if min_distance_to_E is None or popped_distance <= min_distance_to_E:
                for linked in edges[popped]:
                    new_distance = popped_distance + edges[popped][linked][0]
                    if min_distance_to_E is None or min_distance_to_E >= new_distance:
                        if visited[linked] is None or visited[linked] >= new_distance:
                            visited[linked] = new_distance
                            heappush(heap, (new_distance, popped_cnt * edges[popped][linked][1], linked))


        # print('min_dist : {}, min_cnt : {}, heap : {}'.format(min_distance_to_E, min_distance_cnt, heap))

    print(min_distance_cnt % (10**9 + 9))