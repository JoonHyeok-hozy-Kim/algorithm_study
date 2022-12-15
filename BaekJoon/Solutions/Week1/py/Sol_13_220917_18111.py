"""
18111. 마인크래프트
https://www.acmicpc.net/problem/18111
"""


if __name__ == '__main__':
    N, M, B = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]

    from math import inf
    max_height = 256
    result_time = inf
    result_height = max_height

    for trial in range(max_height+1):
        delta = 0
        temp_time = 0
        for i in range(N):
            for j in range(M):
                diff = land[i][j] - (max_height-trial)
                if diff > 0:
                    delta += diff
                    temp_time += 2*diff
                elif diff < 0:
                    delta += diff
                    temp_time -= diff
        if delta + B >= 0:
            if temp_time < result_time:
                result_time = temp_time
                result_height = max_height-trial

    print('{} {}'.format(result_time, result_height))