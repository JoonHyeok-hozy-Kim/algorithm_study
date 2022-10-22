"""
https://www.acmicpc.net/problem/1863
"""


if __name__ == '__main__':
    N = int(input())
    skyline = [list(map(int, input().split())) for _ in range(N)]
    # print(skyline)

    tower_cnt = 0
    S = []
    if skyline[0][1] > 0:
        S.append(skyline[0][1])
    for i in range(1, N):
        while len(S) > 0 and S[-1] > skyline[i][1]:
            tower_cnt += 1
            S.pop()
        if skyline[i][1] > 0 and (len(S) == 0 or (len(S) > 0 and S[-1] != skyline[i][1])):
            S.append(skyline[i][1])
        # print(tower_cnt, S)

    tower_cnt += len(S)
    print(tower_cnt)


