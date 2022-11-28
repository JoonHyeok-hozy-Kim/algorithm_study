"""
https://www.acmicpc.net/problem/16958
"""
from heapq import heappop, heappush
input = __import__('sys').stdin.readline


def calculate_distance(C, T, i, j):
    if i == j:
        return 0
    special = T if C[i][0] + C[j][0] == 2 else None
    ordinary = abs(C[i][1]-C[j][1]) + abs(C[i][2]-C[j][2])
    if special is None:
        return ordinary
    else:
        return min(special, ordinary)


def get_shortest_path_with_map(N, C, T, M, a, b):
    min_distance = None
    heap = []
    heappush(heap, (0, a))
    while heap:
        prev_distance, popped = heappop(heap)

        if min_distance is not None and prev_distance > min_distance:
            continue

        if (popped, b) in M:
            temp = M[(popped, b)]
        elif (b, popped) in M:
            temp = M[(b, popped)]
        else:
            temp = calculate_distance(C, T, popped, b)
            M[(popped, b)] = temp

        new_distance = prev_distance + temp
        if min_distance is None or new_distance < min_distance:
            min_distance = new_distance

        for k in range(1, N+1):
            if k != popped:
                if (popped, k) in M:
                    temp = M[(popped, k)]
                elif (k, popped) in M:
                    temp = M[(k, popped)]
                else:
                    temp = calculate_distance(C, T, popped, k)
                    M[(popped, k)] = temp

                added_distance = prev_distance + temp
                if added_distance < min_distance:
                    heappush(heap, (added_distance, k))

    # print('M : {}'.format(M))
    return min_distance


if __name__ == '__main__':
    N, T = map(int, input().split())
    cities = [None] * (N+1)
    idx = 1
    for _ in range(N):
        cities[idx] = list(map(int, input().split()))
        idx += 1

    distance_record = {}
    M = int(input())
    for _ in range(M):
        A, B = map(int, input().split())
        # result = get_shortest_path(N, cities, T, A, B)
        result = get_shortest_path_with_map(N, cities, T, distance_record, A, B)
        print(result)