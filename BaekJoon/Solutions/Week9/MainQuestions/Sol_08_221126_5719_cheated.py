"""
https://www.acmicpc.net/problem/5719
"""
from heapq import heappop, heappush
from collections import deque


def dijkstra(N, E, start):
    distances = [None] * N
    heap = []
    heap.append((0, start))
    while heap:
        popped_distance, popped = heappop(heap)
        if distances[popped] is not None:
            continue

        distances[popped] = popped_distance
        if E[popped] is not None:
            for linked in E[popped]:
                heappush(heap, (popped_distance+E[popped][linked], linked))

    return distances


def trim_backward(E, ER, FD, end):
    Q = deque()
    Q.append(end)
    while Q:
        popped = Q.popleft()
        if ER[popped] is not None:
            for linked in ER[popped]:
                if FD[linked] is not None and linked in ER[popped] and FD[linked] + ER[popped][linked] == FD[popped]:
                    if popped in E[linked]:
                        del E[linked][popped]
                        Q.append(linked)


if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break

        S, D = map(int, input().split())
        edges = [None] * N
        edges_reverse = [None] * N
        for _ in range(M):
            u, v, p = map(int, input().split())
            if edges[u] is None:
                edges[u] = {}
            edges[u][v] = p

            if edges_reverse[v] is None:
                edges_reverse[v] = {}
            edges_reverse[v][u] = p

        forward_distances = dijkstra(N, edges, S)
        if forward_distances[D] is None:
            print(-1)
        else:
            trim_backward(edges, edges_reverse, forward_distances, D)
            final_distances = dijkstra(N, edges, S)
            if final_distances[D] is None:
                print(-1)
            else:
                print(final_distances[D])