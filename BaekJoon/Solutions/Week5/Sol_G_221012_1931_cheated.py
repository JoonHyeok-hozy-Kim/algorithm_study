"""
1931. 회의실 배정
https://www.acmicpc.net/problem/1931

만약 안풀린다면, 아래 반례 참고
3
1 10
9 12
10 20
"""


if __name__ == '__main__':
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    availables = []

    meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
    # print(meetings)
    target = meetings.pop(0)
    while len(meetings) > 0:
        comp = meetings.pop(0)
        if target[1] > comp[0]:
            if target[1] > comp[1]:
                target = comp
        else:
            availables.append(target)
            target = comp
    availables.append(target)

    # print(availables)
    print(len(availables))