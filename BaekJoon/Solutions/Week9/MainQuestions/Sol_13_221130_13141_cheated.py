"""
https://www.acmicpc.net/problem/13141
"""
from math import inf


def floyd_warshall(D):
    for mid in range(1, N+1):
        for start in range(1, N+1):
            for end in range(1, N+1):
                D[start][end] = min(D[start][end], D[start][mid] + D[mid][end])


def adjust(L, D):
    final_result = inf
    for start in range(1, N+1):
        temp_time_spent = 0

        for _from in range(1, N+1):
            for _to in range(1, N+1):
                if L[_from][_to] is not None:
                    remaining = L[_from][_to] - (D[start][_to] - D[start][_from])
                    if remaining > 0:
                        time_spent = D[start][_to] + remaining/2
                        temp_time_spent = max(time_spent, temp_time_spent)

        final_result = min(final_result, temp_time_spent)

    return final_result


if __name__ == '__main__':
    N, M = map(int, input().split())
    longests = [[None] * (N+1) for _ in range(N+1)]
    distances = [[inf] * (N+1) for _ in range(N+1)]

    for m in range(M):
        s, e, l = map(int, input().split())
        if longests[s][e] is None or longests[s][e] < l:
            longests[s][e] = longests[e][s] = l
        if distances[s][e] > l:
            distances[s][e] = distances[e][s] = l

    # print('distances : {}'.format(distances))
    floyd_warshall(distances)
    # print('distances : {}'.format(distances))
    result = adjust(longests, distances)
    # print('distances : {}'.format(distances))
    print(result)
