"""
https://www.acmicpc.net/problem/1007
"""


def get_distance(x, y):
    return pow(pow(x, 2) + pow(y, 2), .5)


def recursive_sol(P, i=0, x=0, y=0, pos_cnt=0, neg_cnt=0, min_val=None):
    if i == len(P):
        return get_distance(x, y)

    if pos_cnt < len(P)//2:
        temp = recursive_sol(P, i+1, x+P[i][0], y+P[i][1], pos_cnt+1, neg_cnt, min_val)
        min_val = min(min_val, temp) if min_val is not None else temp

    if neg_cnt < len(P)//2:
        temp = recursive_sol(P, i+1, x-P[i][0], y-P[i][1], pos_cnt, neg_cnt+1, min_val)
        min_val = min(min_val, temp) if min_val is not None else temp

    return min_val


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = [list(map(int, input().split())) for _ in range(N)]
        # print(points)

        print(recursive_sol(points))