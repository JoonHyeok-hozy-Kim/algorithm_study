"""
https://www.acmicpc.net/problem/2171
"""
from bisect import bisect_left, bisect_right


if __name__ == '__main__':
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    x_map = {}
    y_map = {}

    for i in range(N):
        p = points[i]
        if p[0] not in x_map:
            x_map[p[0]] = {}
        if p[1] not in x_map[p[0]]:
            x_map[p[0]][p[1]] = True

        if p[1] not in y_map:
            y_map[p[1]] = {}
        if p[0] not in y_map[p[1]]:
            y_map[p[1]][p[0]] = True
    # print(x_map)
    # print(y_map)

    result = 0
    for i in range(N):
        for j in range(i+1, N):
            p1, p2 = points[i], points[j]
            if p1[0] != p2[0] and p1[1] != p2[1]:
                if p2[1] in x_map[p1[0]] and p2[0] in y_map[p1[1]]:
                    # print(p1, p2)
                    result += 1


    print(result//2)