"""
https://www.acmicpc.net/problem/11812
"""
input = __import__('sys').stdin.readline
from bisect import bisect_left


def K_is_one_sol(N, Q):
    for _ in range(Q):
        x, y = map(int, input().split())
        print(abs(x-y))


def K_is_not_one_sol(N, K, Q):
    breadth_end = [1]
    end, power = 1, 1
    while end < N:
        power *= K
        end += power
        breadth_end.append(end)
    # print(breadth_end)
    # print(len(breadth_end))

    for _ in range(Q):
        x, y = map(int, input().split())
        d = get_distance(K, breadth_end, x, y)
        print(d)


def get_distance(K, B, x, y):
    cnt = 0
    xi = bisect_left(B, x)
    yi = bisect_left(B, y)
    while x != y:
        if xi > yi:
            x = get_upper_level_num(K, B, x, xi)
            xi -= 1
            cnt += 1

        elif xi < yi:
            y = get_upper_level_num(K, B, y, yi)
            yi -= 1
            cnt += 1

        else:
            x = get_upper_level_num(K, B, x, xi)
            xi -= 1
            y = get_upper_level_num(K, B, y, yi)
            yi -= 1
            cnt += 2

    return cnt


def get_upper_level_num(K, B, z, zi):
    temp = z - B[zi] - 1
    temp //= K
    if zi == 0:
        return temp
    else:
        return B[zi-1] + temp + 1


if __name__ == '__main__':
    N, K, Q = map(int, input().split())

    if K == 1:
        K_is_one_sol(N, Q)

    else:
        K_is_not_one_sol(N, K, Q)


"""
         0
  1      2        3
4 5 6  7 8 9  10 11 12

1000000000000000 2 1
950000000000000 99999999999999
"""