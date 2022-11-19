"""
https://www.acmicpc.net/problem/11812
"""
from bisect import bisect_left


def get_distance(K, B, x, y):
    cnt = 0
    while x != y:
        xi = bisect_left(B, x)
        yi = bisect_left(B, y)

        if xi > yi:
            None
            cnt += 1
        elif xi < yi:
            None
            cnt += 1
        else:
            None
            cnt += 2


def get_upper_level_num(K, B, z, zi):
    temp = z - B[zi] - 1
    temp //= K



if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    breadth_end = [1]
    end, power = 1, 1
    while end < N:
        power *= K
        end += power
        breadth_end.append(end)
    print(breadth_end)

    for _ in range(Q):
        x, y = map(int, input().split())
        d = get_distance(K, breadth_end, x, y)


"""
         0
  1      2        3
4 5 6  7 8 9  10 11 12

"""