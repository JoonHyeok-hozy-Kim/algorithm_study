"""
https://www.acmicpc.net/problem/1854
"""
from heapq import heappop, heappush
input = __import__('sys').stdin.readline


def dijkstra_k(N, E, K):
    distances = [[] for _ in range(N+1)]
    distances[1] = [(0, 0)]
    heap = []
    heappush(heap, (0, 1))
    while heap:
        popped_distance, popped = heappop(heap)
        # print('distances : {}'.format(distances))

        if E[popped] is not None:
            for linked in E[popped]:
                if len(distances[linked]) == 0:
                    E[popped][linked].sort()

                for additional in E[popped][linked]:
                    new_distance = popped_distance + additional
                    if len(distances[linked]) < K:
                        heappush(distances[linked], (-new_distance, new_distance))
                        heappush(heap, (new_distance, linked))
                    elif distances[linked][0][1] > new_distance:
                        heappop(distances[linked])
                        heappush(distances[linked], (-new_distance, new_distance))
                        heappush(heap, (new_distance, linked))

    return distances


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    edges = [None] * (N+1)
    for _ in range(M):
        a, b, c = map(int, input().split())
        if edges[a] is None:
            edges[a] = {}
        if b not in edges[a]:
            edges[a][b] = []
        edges[a][b].append(c)
        # print(edges)

    result = dijkstra_k(N, edges, K)
    # print(result)
    for i in range(1, N+1):
        if len(result[i]) < K:
            print(-1)
        else:
            x = len(result[i])
            while x > K:
                heappop(result[i])
                x -= 1
            print(result[i][0][1])