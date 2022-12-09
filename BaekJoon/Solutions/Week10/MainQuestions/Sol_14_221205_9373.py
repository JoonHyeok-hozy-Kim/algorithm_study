"""
https://www.acmicpc.net/problem/9373
"""
from heapq import heappush, heappop


def get_available_radius(a, b):
    dist = (a[0]-b[0])**2
    dist += (a[1]-b[1])**2
    dist **= .5
    return (dist - (a[2]+b[2])) / 2


def find(p, x):
    if x < 0:
        return x
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return find(p, p[x])


def union(p, x, y):
    if x == y:
        return x
    px, py = find(p, x), find(p, y)
    if px <= py:
        p[py] = px
        return px
    else:
        p[px] = py
        return py


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        w = int(input())
        n = int(input())
        result = None
        if n == 0:
            result = w/2

        else:
            sensors = [None] * n
            lefties = [None] * n
            righties = [None] * n
            parents = [i for i in range(n)]
            radii = [[None] * n for _ in range(n)]
            for i in range(n):
                sensors[i] = tuple(map(int, input().split()))
                lefties[i] = sensors[i][0] - sensors[i][2]
                righties[i] = (w - sensors[i][0]) - sensors[i][2]

            # print('sensors : {}'.format(sensors))
            # print('lefties : {}'.format(lefties))
            # print('righties : {}'.format(righties))

            if result is None:
                heap = []
                candidates = []
                for i in range(n):
                    for j in range(n):
                        pi, pj = find(parents, i), find(parents, j)
                        if pi == pj:
                            continue

                        temp_radius = get_available_radius(sensors[i], sensors[j])
                        if temp_radius <= 0:
                            k = union(parents, pi, pj)
                            lefties[k] = min(lefties[pi], lefties[pj])
                            righties[k] = min(righties[pi], righties[pj])

                        else:
                            radii[i][j] = temp_radius

                # print('parents : {}'.format(parents))
                # print('lefties : {}'.format(lefties))
                # print('righties : {}'.format(righties))
                # print('candidates : {}'.format(candidates))
                for p in set(parents):
                    if lefties[p] <= 0 and righties[p] <= 0:
                        result = 0
                        break
                    heappush(candidates, (max(lefties[p], righties[p])*(.5), p, -1))
                    # print('candidates : {}'.format(candidates))

                if result is None:
                    while candidates:
                        r, i, j = heappop(candidates)
                        if find(parents, i) != find(parents, j):
                            result = r
                            break

                if result is None:
                    result = 0

        print(round(result, 6))


"""
1
10
4
1 2 3
4 2 2
7 2 1
9 2 1


1
10
4
1 2 3
4 2 2
7 2 1
7 6 3

1
10
4
1 2 3
4 2 2
7 2 1
7 20 2
"""