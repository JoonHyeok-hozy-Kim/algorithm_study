"""
https://www.acmicpc.net/problem/1425
"""


if __name__ == '__main__':
    N = int(input())
    x_map = {}
    max_dist = 0

    for _ in range(N):
        x, y = map(int, input().split())
        if x not in x_map:
            x_map[x] = []
        x_map[x].append(y)

    for x in x_map.keys():
        x_map[x].sort()

    print(x_map)

    for x in x_map.keys():
        max_dist = max(max_dist, abs(x_map[x][0] - x_map[x][-1]))
        vertical_max = max(abs(x_map[x][0]), abs(x_map[x][-1]))
        x_map[x] = vertical_max

    print(max_dist)
    print(x_map)