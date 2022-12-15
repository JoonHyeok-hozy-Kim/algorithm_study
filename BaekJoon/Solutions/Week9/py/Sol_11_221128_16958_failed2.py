"""
https://www.acmicpc.net/problem/16958
"""
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


def first_fill(T, C, D):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if start != end and D[start][end] is None and D[start][end] is None:
                D[start][end] = D[start][end] = calculate_distance(C, T, start, end)


def floyd_warshall(N, D):
    for mid in range(1, N+1):
        for start in range(1, N+1):
            for end in range(1, N+1):
                if start == end or start == mid or end == mid:
                    continue
                D[start][end] = min(D[start][end], D[start][mid] + D[mid][end])


if __name__ == '__main__':
    N, T = map(int, input().split())
    cities = [None] * (N+1)
    for i in range(1, N+1):
        cities[i] = list(map(int, input().split()))

    distance_record = [[None] * (N+1) for _ in range(N+1)]
    first_fill(T, cities, distance_record)
    # print(distance_record)
    floyd_warshall(N, distance_record)
    # print(distance_record)

    M = int(input())
    for _ in range(M):
        A, B = map(int, input().split())
        print(distance_record[A][B])